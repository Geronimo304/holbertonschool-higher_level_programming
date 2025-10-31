#!/usr/bin/python3
"""
Script that connects to a MySQL database and retrieves states
matching a specific name.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>
        <state_name>

Arguments:
    mysql_username  - The MySQL username
    mysql_password  - The MySQL password
    database_name   - The name of the database to connect to
    state_name      - The name of the state to search for

Example:
    ./script_name.py root password hbtn_0e_0_usa Texas
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
        (
            "SELECT * FROM states WHERE name = '{}'"
            "COLLATE utf8_bin ORDER BY id ASC"
        ).format(av[3])
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
