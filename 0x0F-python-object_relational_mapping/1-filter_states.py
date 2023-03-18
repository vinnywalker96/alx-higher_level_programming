#!/usr/bin/python3
"""This script that lists all states with a name starting with N
from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    obj = db.cursor()
    obj.execute("SELECT * FROM states WHERE\
                 name LIKE BINARY 'N%' ORDER BY states.id ASC")
    rows = obj.fetchall()
    for row in rows:
        print(row)
    obj.close()
    db.close()
