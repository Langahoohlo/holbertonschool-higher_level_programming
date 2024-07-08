#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """
    Connects to the MySQL server and lists
    all cities from the specified database.

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
        query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """
        cursor.execute(query)
        cities = cursor.fetchall()
        for city in cities:
            print(city)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("""
        Usage: ./4-cities_by_state.py <username>
        <password> <database>
        """)
