#!/usr/bin/python3
""" script that lists all states"""

import MySQLdb
import sys

def list_states(username, password, database):
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
    	if state[1][0] == 'N':
        	print(state)

    db.close()

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, database)
