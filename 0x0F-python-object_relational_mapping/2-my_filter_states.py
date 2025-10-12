#!/usr/bin/env python3


import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    username, password, database, name = arg[1], arg[2], arg[3], arg[4]

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306
                         )
    cur = db.cursor()

    statement = f"SELECT * FROM states WHERE name = '{name}' ORDER BY id ASC"
    cur.execute(statement)
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
