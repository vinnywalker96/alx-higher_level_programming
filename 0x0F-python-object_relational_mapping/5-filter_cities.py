#!/usr/bin/python3
"""This script that takes in the name
of a state as an argument and lists all cities
"""
import sys
import MySQLdb as db

[USERNAME, PASSWORD, DB_NAME, STATE_NAME] = sys.argv[1:5]


def filter_cities():
    conn = db.connect(
           host='localhost',
           user=USERNAME,
           passwd=PASSWORD,
           db=DB_NAME,
           port=3306)
    obj = conn.cursor()
    obj.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON
                states.id=cities.state_id
                WHERE states.name=%s""", (STATE_NAME,))
    rows = obj.fetchall()
    res = list(row[0] for row in rows)
    print(*res, sep=", ")
    obj.close()
    conn.close()


if __name__ == "__main__":
    filter_cities()
