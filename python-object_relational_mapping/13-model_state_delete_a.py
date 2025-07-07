#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>
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

    # Obtener todos los estados que contienen 'a' en el nombre
    states_to_delete = (
        session.query(State).filter(State.name.like("%a%")).all()
    )

    for state in states_to_delete:
        session.delete(state)

    session.commit()
