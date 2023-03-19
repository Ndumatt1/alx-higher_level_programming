#!/usr/bin/python3
''' This module changes the name of a State object'''
if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    user, pswd, db = argv[1:4]
    engine = create_engine(f'mysql+mysqldb://{user}:{pswd}@localhost/{db}')
    session = Session(engine)
    query = session.query(State).filter(State.id == 2).first()
    query.name = 'New Mexico'
    session.commit()
