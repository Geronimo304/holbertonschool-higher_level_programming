#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""

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
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
