#!/usr/bin/env python3

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db =database,
                         port=3306
                         )
    cur = db.cursor()
    statement = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    cur.execute(statement)
    states = cur.fetchall()
    
    for state in states:
        print(state)

    cur.close()
    db.close()
