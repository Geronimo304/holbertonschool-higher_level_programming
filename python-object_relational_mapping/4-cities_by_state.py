#!/usr/bin/python3
"""
Lists all cities from the database passed as argument.

The script connects to a MySQL database using the provided credentials and
retrieves all cities along with their corresponding state names. Results
are sorted by cities.id in ascending order.

Usage:
    ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username  - MySQL username
    mysql_password  - MySQL password
    database_name   - Name of the database
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
        "SELECT cities.id, cities.name, states.name FROM cities "
        "JOIN states ON states.id = cities.state_id "
        "ORDER BY cities.id ASC"
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
