#!/usr/bin/python3
''' This module prints State objects with the name passed as argument'''
if __name__ == '__main__':
    from model_state import Base, State
    from sys import argv
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

    user, pswd, db, name = argv[1:5]
    engine = create_engine(f'mysql+mysqldb://{user}:{pswd}@localhost/{db}')
    session = Session(engine)
    query = session.query(State).filter(State.name == name).first()
    if query is None:
        print('Not found')
    else:
        print(query.id)
