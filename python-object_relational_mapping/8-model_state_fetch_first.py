#!/usr/bin/python3
"""
Module to retrieve and print the State object with id=1 from a MySQL database.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server on localhost at port 3306, queries the
State table for the record with id=1, and prints its id and name.

If no such State exists, it prints "Nothing".
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    av = sys.argv[1:]
    engine = create_engine(
        f"mysql+mysqldb://{av[0]}:{av[1]}@localhost:3306/{av[2]}",
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 1).one_or_none()

    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
