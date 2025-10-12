#!/usr/bin/env python3
"""
script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""


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

    statement = "SELECT cities.name FROM cities INNER JOIN states ON states.id = cities.state_id WHERE states.name = %s ORDER BY cities.id"

    cur.execute(statement, (name,))
    cities = cur.fetchall()
    
    print(", ".join([city[0] for city in cities]) )

    cur.close()
    db.close()
