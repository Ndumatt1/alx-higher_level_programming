#!/usr/bin/python3
''' This module prints the first State object
from the database hbtn_0e_6_usa
'''
from model_state import Base, State
from sqlalchemy.orm import Session
from sys import argv
from sqlalchemy import create_engine

if __name__ == '__main__':
    user = argv[1]
    pswd = argv[2]
    db = argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{pswd}@localhost/{db}')
    session = Session(engine)
    query = session.query(State).first()
    if query is None:
        print('Nothing')
    else:
        print('{}: {}'.format(query.id, query.name))
