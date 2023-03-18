#!/usr/bin/python3
"""This script that lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb as db

if __name__ == "__main__":
    conn = db.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3307)
    obj = conn.cursor()
    obj.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    result = obj.fetchall()
    for res in result:
        print(res)
    obj.close()
    conn.close()
