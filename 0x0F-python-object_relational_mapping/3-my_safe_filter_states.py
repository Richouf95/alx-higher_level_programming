#!/usr/bin/python3
"""
a script that lists all states with a name match
user input and make it SAFE from the database hbtn_0e_0_usa
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
    cursor.execute("""SELECT * FROM states WHERE name
                LIKE BINARY %s ORDER BY states.id""", (sys.argv[4], ))
    rows = cursor.fetchall()

    for r in rows:
        print(r)

    cursor.close()
    dataBase.close()
