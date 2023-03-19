#!/usr/bin/python3
''' This module lists all State objects that contain the letter a '''
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == '__main__':
    user, pswd, db = argv[1:4]

    engine = create_engine(f'mysql+mysqldb://{user}:{pswd}@localhost/{db}')
    session = Session(engine)
    qry = session.query(State) \
        .filter(State.name.like('%a%')).order_by(State.id).all()
    for states in qry:
        print(f'{states.id}: {states.name}')
