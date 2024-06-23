#!/usr/bin/python3
"""
Script to print the first State object
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state(username, password, database):
    """
    Connects to the MySQL server and prints
    the first State object from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
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

        # Query the first State object and display it
        first_state = session.query(State).order_by(State.id).first()
        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        session.close()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        fetch_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("""
        Usage: ./8-model_state_fetch_first.py <username> <password>
        <database>
        """)
