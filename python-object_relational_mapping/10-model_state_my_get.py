#!/usr/bin/python3
"""
Script to print the State object with the name
passed as argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_by_name(username, password, database, state_name):
    """
    Connects to the MySQL server and prints the id
    of the State object with the specified name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to search for.
    """
    try:
        # Connect to the MySQL server
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                username, password, database
            ),
            pool_pre_ping=True
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the State object with the specified name and display its id
        state = session.query(State).filter(State.name == state_name).first()
        if state:
            print(state.id)
        else:
            print("Not found")

        session.close()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 5:
        get_state_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("""
        Usage: ./10-model_state_my_get.py <username> <password> <database>
        <state_name>
        """)
