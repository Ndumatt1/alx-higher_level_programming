#!/usr/bin/python3
''' This module lists all cities from the database hbtn_0e_4_usa'''
if __name__ == '__main__':
    import sys
    import MySQLdb

    username, password, db_name = sys.argv[1:4]

    connect = MySQLdb.connect('localhost', username, password, db_name)

    cursor = connect.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN \
            states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cursor.execute(query)
    records = cursor.fetchall()
    for record in records:
        print(record)
