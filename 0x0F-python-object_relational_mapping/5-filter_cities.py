#!/usr/bin/python3
'''
This module takes in the name of a state as an argument and lists all cities
of that state
'''
if __name__ == '__main__':
    import sys
    import MySQLdb

    username, password, db_name, name = sys.argv[1:5]

    connect = MySQLdb.connect('localhost', username, password, db_name)
    cursor = connect.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON \
            cities.state_id = states.id WHERE states.name = %s"
    cursor.execute(query, (name,))
    records = cursor.fetchall()
    new_list = []
    for record in records:
        new_list.append(record[0])
    print(', '.join(new_list))
