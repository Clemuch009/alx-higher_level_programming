#!/usr/bin/env python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ =="__main__":
    arglist = sys.argv[1:]
    username = arglist[0]
    passkey = arglist[1]
    database = arglist[2]
    db = MySQLdb.connect(host='localhost',
                     user=username,
                     password=passkey,
                     port=3306,
                     db = database
                     )
    cur = db.cursor()
    statement = "SELECT * FROM states ORDER BY states.id ASC"
    states = cur.execute(statement)
    
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
