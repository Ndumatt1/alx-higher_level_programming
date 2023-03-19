#!/usr/bin/python3
'''
This module takes an argument and displays all values in the states table
where name matches the argument. This query is safe from mysql injections
'''
if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]

    connect = MySQLdb.connect('localhost', username, password, db_name)
    cursor = connect.cursor()
    query = "SELECT * FROM states WHERE name = \
            %s ORDER BY states.id ASC"
    cursor.execute(query, (name,))
    records = cursor.fetchall()
    for record in records:
        print(record)
