#!/usr/bin/python3
"""
Prints the id of the State object with the name passed
as argument from the database.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound
from model_state import Base, State

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1:5]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(State.name == state_name).one()
        print(state.id)
    except NoResultFound:
        print("Not found")
