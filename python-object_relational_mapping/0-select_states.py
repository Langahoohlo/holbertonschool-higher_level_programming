#!/usr/bin/python3
"""List all states from hbtn_0e_0_usa db"""


if __name__ == "__main__":
    import MySQLdb
    import sys

# Establish connection using MySQLdb
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

# Create cursor object to interact with db by executing SQL queries
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    # fetchall() retrieves all rows returned from SQL query in execute()
    rows = cur.fetchall()
# Returns list of tuples. Each tuple is a row from the result set of the query
    for row in rows:
        print("({0}, '{1}')".format(row[0], row[1]))
