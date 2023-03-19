#!/usr/bin/python3
''' This module lists all State ibjects from the database hbtn_0e_6_usa'''
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv

user = argv[1]
passwd = argv[2]
db_name = argv[3]

engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db_name}')

session = Session(engine)

query = session.query(State).order_by(State.id).all()

for state in query:
    print('{}: {}'.format(state.id, state.name))
session.close()
