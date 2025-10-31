#!/usr/bin/python3
"""
Updates the name of the State object with id = 2 to "New Mexico"
in the database hbtn_0e_6_usa.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]

    # Crear conexión al motor de MySQL
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar el State con id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Si existe, modificar su nombre
    if state:
        state.name = "New Mexico"
        session.commit()
