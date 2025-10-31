#!/usr/bin/python3
"""
Script that lists states from a MySQL database that match a given name.
Comparison is case-sensitive using COLLATE utf8_bin.

Usage:
    ./2-my_filter_states.py <username> <password> <database> <state_name>
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
    cur.execute(
        "SELECT * FROM states WHERE name = %s "
        "COLLATE utf8_bin ORDER BY id ASC",
        (av[3],),
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
