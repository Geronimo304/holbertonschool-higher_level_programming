#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
Format: <state name>: (<city id>) <city name>

Usage:
    ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True,
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(City).join(State).order_by(City.id).all()

    for city in results:
        print(f"{city.state.name}: ({city.id}) {city.name}")
