#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities
of that state using the database hbtn_0e_4_usa
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
            SELECT cities.name
            FROM cities
            INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s
            """, (sys.argv[4], ))
    rows = cursor.fetchall()

    cities = []

    for r in rows:
        cities.append(r[0])

    print(*cities, sep=", ")

    cursor.close()
    dataBase.close()
