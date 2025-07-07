#!/usr/bin/python3
"""
Imprime todas las ciudades de la BD `hbtn_0e_14_usa`, mostrando
<state name>: (<city id>) <city name>
ordenadas por `cities.id`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Argumentos: usuario, contraseña y nombre de la BD
    if len(sys.argv) != 4:
        sys.exit("Uso: ./14-model_city_fetch_by_state.py <user> <password> <db>")

    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    # Crear engine y sesión
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}",
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: unimos State y City, ordenamos por City.id
    results = (
        session.query(State.name, City.id, City.name)
        .join(City)
        .order_by(City.id.asc())
        .all()
    )

    # Imprimir en el formato solicitado
    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")
