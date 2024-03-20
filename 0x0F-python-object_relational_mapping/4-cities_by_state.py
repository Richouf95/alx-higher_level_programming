#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    dataBase = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cursor = dataBase.cursor()
    cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON states.id=cities.state_id
            """)
    rows = cursor.fetchall()

    for r in rows:
        print(r)

    cursor.close()
    dataBase.close()
