#!/usr/bin/python3
''' This module lists all State ibjects from the database hbtn_0e_6_usa'''
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    pswd = argv[2]
    db = argv[3]

    engine = create_engine(f'mysql+mysqldb://{user}:{pswd}@localhost/{db}')

    session = Session(engine)

    query = session.query(State).order_by(State.id).all()

    for state in query:
        print('{}: {}'.format(state.id, state.name))
