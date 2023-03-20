#!/usr/bin/python3
''' This module defines an ORM model'''
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative()


class State(Base):
    ''' Inherits from declarative_base and Defines a model'''
    __table__name = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    state = relationship('cities', backref='states', cascade='all, delete, delete-orphan')
