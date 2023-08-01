#!/usr/bin/python3
""" script that lists all states"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    name = sys.argv[4]
    request = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(request, (name,))
    states = cursor.fetchall()
    
    for state in states:
        print(state)
    cursor.close()
    db.close
