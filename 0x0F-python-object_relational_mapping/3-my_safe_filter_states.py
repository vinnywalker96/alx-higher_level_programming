#!/usr/bin/python3
"""script that takes in arguments and
displays all values in the states table """

import sys
import MySQLdb as db

if __name__ == "__main__":
    conn = db.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    obj = conn.cursor()
    obj.execute("SELECT * FROM states WHERE\
                 name IN ('{}') ORDER BY states.id".format(sys.argv[4]))
    rows = obj.fetchall()
    for row in rows:
        print(row)
    obj.close()
    conn.close()
