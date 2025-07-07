#!/usr/bin/python3

"""
Lists all city names from the given state in a MySQL database.

The script connects to a MySQL database using the credentials provided
via command-line arguments, then retrieves all cities belonging to the
specified state. The city names are printed as a comma-separated list,
ordered by city ID ascending.

Usage:
    ./script.py <mysql_username> <mysql_password> <database_name> <state_name>

Arguments:
    mysql_username  - MySQL username
    mysql_password  - MySQL password
    database_name   - Name of the database to connect to
    state_name      - Name of the state to filter cities by

Output:
    Prints city names on a single line separated by commas.
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
        "SELECT cities.name FROM cities "
        "JOIN states ON states.id = cities.state_id WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (av[3],),
    )
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
