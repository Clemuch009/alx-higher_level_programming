#!/usr/bin/env python3
"""
 script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    username, password, database = arg[1], arg[2], arg[3]

    db = MySQLdb.connect(host='localhost',
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306
                         )
    cur = db.cursor()
    
    statement = "SELECT cities.id, cities.name, states.name  FROM  cities INNER JOIN states ON states.id = state_id ORDER BY id ASC"
    cur.execute(statement)
    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
