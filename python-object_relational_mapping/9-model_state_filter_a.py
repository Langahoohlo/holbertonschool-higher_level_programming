#!/usr/bin/python3
"""
This script lists all State objects that
contain the letter 'a' from the database hbtn_0e_6_usa

args:
    username (str): the username for the mysql database
    password (str): the password for the mysql database
    database (str): the name of the mysql database containing
    the states table
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name.like('%a%')).order_by(
        State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
