#!/usr/bin/python3
"""
Script that takes an argument and displays all values in the
states table from hbtn_0e_0_usa where name matches the argument
and also safe from MySQL injections
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s;", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)
