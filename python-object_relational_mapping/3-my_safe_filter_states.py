#!/usr/bin/python3
""" Conects to a database"""


if __name__ == "__main__":
    """ conects to a database"""

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         database=sys.argv[3],
                         user=sys.argv[1],
                         password=sys.argv[2])
    cursor = db.cursor()
    input = sys.argv[4]
    cursor.execute("SELECT * FROM states \
        WHERE name = %s ORDER BY id ASC", (input, ))
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
