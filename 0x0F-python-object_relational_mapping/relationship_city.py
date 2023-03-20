#!/usr/bin/python3
''' This module contains class definition of a city'''
from model_state import Base
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy import (create_engine)
from sqlalchemy.orm import relationship


class City(Base):
    ''' Class City that inherits from Base'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State', backref='cities')
