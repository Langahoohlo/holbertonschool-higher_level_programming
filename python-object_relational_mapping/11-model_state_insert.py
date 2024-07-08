#!/usr/bin/python3
"""
Script to add the State object "Louisiana"
to the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_state(username, password, database):
    """
    Connects to the MySQL server and adds the State
    object "Louisiana" to the specified database.

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

        # Create a new State object for Louisiana and add it to the session
        louisiana = State(name="Louisiana")
        session.add(louisiana)
        session.commit()

        # Print the id of the newly created State object
        print(louisiana.id)

        session.close()
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        insert_state(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("""
        Usage: ./11-model_state_insert.py <username> <password>
        <database>""")
