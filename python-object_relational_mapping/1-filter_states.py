#!/usr/bin/python3
"""
Script to list all states with a name starting with
'N' (upper N) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Connects to the MySQL server and lists all states
    with a name starting with 'N'.

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
        cursor.execute("""SELECT * FROM states WHERE name
                       LIKE BINARY 'N%' ORDER BY states.id""")
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./1-filter_states.py <username> <password> <database>")
