#!/usr/bin/python3
''' 
This module takes in an argument and displays all values in the states
table where name matches the argument
'''
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    query_name = sys.argv[4]

    connect = MySQLdb.connect("localhost", username, password, db_name)
    curs = connect.cursor()
    sql = 'SELECT * FROM states WHERE name = {query} ORDER BY states.id'
    qry = sql.format(query=query_name)
    curs.execute(qry)

    '''   curs.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id").format(query_name)'''
    records = curs.fetchall()
    for record in records:
        print(record)
