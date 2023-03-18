#!/usr/bin/python3
"""
This module selects all states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    conn = MySQLdb.connect("localhost", username, password, dbname)

    cursor = conn.cursor()
    records = cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    records = cursor.fetchall()
    for record in records:
        print(record)
