#!/usr/bin/python3
""" Conects to a database"""
import MySQLdb
import sys

if __name__ == "__main__":
    """ conects to a database"""

    db = MySQLdb.connect(host="localhost",
                         database=sys.argv[3],
                         user=sys.argv[1],
                         password=sys.argv[2])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query = sys.argv[4]
    for row in cursor.fetchall():
        if row[1] == query:
            print("{}".format(row))

    db.close()
