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
    cursor.execute(
        "SELECT cities.id,cities.name,states.name FROM cities INNER JOIN states ON states.id = cities.state_id ORDER BY id ASC")
    for row in cursor.fetchall():
        print("{}".format(row))

    db.close()
