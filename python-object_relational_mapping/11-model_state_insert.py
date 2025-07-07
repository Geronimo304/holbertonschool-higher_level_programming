#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>

Connects to a MySQL server on localhost:3306 and prints
the id of the new state.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
