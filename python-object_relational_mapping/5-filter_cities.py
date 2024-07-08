#!/usr/bin/python3
"""
Script to list all cities of a specified state
from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
    """
    Lists all cities of the specified state from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to filter cities.

    Returns:
        list: List of cities in the specified state.
    """
    cities = []

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()

        # Execute SQL query to retrieve cities of the specified state
        cursor.execute("SELECT cities.name FROM cities "
                       "JOIN states ON cities.state_id = states.id "
                       "WHERE states.name = %s "
                       "ORDER BY cities.id ASC", (state_name,))

        # Fetch all results
        rows = cursor.fetchall()

        # Extract city names from results
        cities = [row[0] for row in rows]

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    return cities


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("""
        Usage: ./5-filter_cities.py <username>
        <password> <database> <state_name>
        """)
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    # Call the function to filter cities by state
    cities = filter_cities(username, password, database, state_name)

    # Print the list of cities
    print(", ".join(cities))
