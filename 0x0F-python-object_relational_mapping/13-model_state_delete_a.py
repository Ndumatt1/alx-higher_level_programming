#!/usr/bin/python3
''' This module deletes all State objects with a name containing letter a'''

if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from sys import argv

    user, pswd, db = argv[1:4]
    engine = create_engine(f'mysql+mysqldb://{user}:{pswd}@localhost/{db}')
    session = Session(engine)
    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
