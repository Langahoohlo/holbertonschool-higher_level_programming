#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to the MySQL server and lists all states from
    the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./0-select_states.py <username> <password> <database>")
