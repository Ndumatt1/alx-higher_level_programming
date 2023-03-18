#!/usr/bin/python3
''' This Module lists all states with name starting with N'''
if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    connect = MySQLdb.connect('localhost', username, password, db_name)
    cursor = connect.cursor()

    cursor.execute('SELECT * FROM states WHERE states.name LIKE %s ORDER BY states.id', ('N%',))
    records = cursor.fetchall()
    for record in records:
        print(record)
