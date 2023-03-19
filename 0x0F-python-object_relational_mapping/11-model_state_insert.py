#!/usr/bin/python3
'''
This module adds a new object to the State model
'''
if __name__ == '__main__':
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sys import argv

    user, pswd, db = argv[1:4]
    engine = create_engine(f'mysql+mysqldb://{user}:{pswd}@localhost/{db}')
    session = Session(engine)

    new_object = State(name='Louisiana')
    session.add(new_object)
    session.commit()
    print(new_object.id)
    session.close()    
