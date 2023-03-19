#!/usr/bin/python3
''' This module prints all City objects '''
if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City

    user, pswd, db = argv[1:4]
    engine = create_engine(f'mysql+mysqldb://{user}:{pswd}@localhost/{db}')
    session = Session(engine)
    query = session.query(City).join(State, City.state_id == State.id). \
        order_by(City.id).all()
    for record in query:
        print(f'{record.state.name}: ({record.id}) {record.name}')
