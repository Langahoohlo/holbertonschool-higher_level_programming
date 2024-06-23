#!/usr/bin/python3
"""
Script to display all values in the states table
of hbtn_0e_0_usa where name matches the argument,
while preventing MySQL injections.
"""

import MySQLdb
import sys


def safe_filter_states_by_name(username, password, database, state_name):
    """
    Connects to the MySQL server and displays all values
    in the states table where name matches the argument.
    Prevents MySQL injections by using parameterized queries.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to search for.
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
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 5:
        safe_filter_states_by_name(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
        )
    else:
        print("""
        Usage: ./3-my_safe_filter_states.py
        <username> <password> <database> <state_name>
        """)
