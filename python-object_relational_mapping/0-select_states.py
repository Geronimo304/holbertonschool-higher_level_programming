#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves all rows
from the 'states' table, ordered by their ID in ascending order.

Usage:
    ./script_name.py <username> <password> <database_name>

Example:
    ./0-select_states.py root mypassword hbtn_0e_0_usa

Modules:
    sys - to retrieve command-line arguments
    MySQLdb - to connect and interact with a MySQL database
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    av = sys.argv[1:]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=av[0],
        passwd=av[1],
        db=av[2],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
