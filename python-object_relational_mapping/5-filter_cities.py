#!/usr/bin/python3
""" Conects to a database"""


if __name__ == "__main__":
    """ conects to a database"""

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         database=sys.argv[3],
                         user=sys.argv[1],
                         password=sys.argv[2])
    cursor = db.cursor()
    str = ""
    cursor.execute(
        "SELECT cities.name FROM states INNER JOIN cities ON cities.state_id = states.id WHERE states.name = %s", (sys.argv[4],))
    for row in cursor.fetchall():
        print(str, end="")
        str = ", "
        print("{}".format(row[0]), end="")
    print()
    db.close(),
