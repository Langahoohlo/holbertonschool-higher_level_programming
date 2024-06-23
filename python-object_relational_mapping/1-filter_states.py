#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa.

Args:
    username: name of the mysql user.
    password: password of the mysql user.
    database: name of the mysql database.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    select = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(select)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
