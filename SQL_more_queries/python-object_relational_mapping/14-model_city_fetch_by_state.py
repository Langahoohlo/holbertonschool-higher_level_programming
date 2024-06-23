#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa

Args:
    - username (str): The username for the MySQL database.
    - password (str): The password for the MySQL database.
    - database (str): The name of the MySQL database
    containing the 'cities' table

The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id.
Results are displayed as <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(
        State, City.state_id == State.id).order_by(City.id).all()

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
