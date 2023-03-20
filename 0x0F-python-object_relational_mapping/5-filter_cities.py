#!/usr/bin/python3
"""This script that takes in the name 
of a state as an argument and lists all cities
"""
import sys
import MySQLdb as db

[USERNAME, PASSWORD, DB_NAME, STATE_NAME] = sys.argv[1:5]
def filter_cities() -> None:
    conn = db.connect()
    

if __name__ == "__main__":
    filter_cities()
