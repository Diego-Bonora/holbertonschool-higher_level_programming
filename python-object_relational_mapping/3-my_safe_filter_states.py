#!/usr/bin/python3
""" Conects to a database"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Conects to a database"""
    db_conection = MySQLdb.connect(host='localhost',
                                   database=argv[3],
                                   user=argv[1],
                                   password=argv[2])
    cursor = db_conection.cursor()
    mySql_select_states = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(mySql_select_states)
    query = argv[4]
    for row in cursor.fetchall():
        if row[1] == query:
            print("{}".format(row))
    db_conection.close()
