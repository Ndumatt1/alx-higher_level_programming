#!/usr/bin/python3
''' This module defines an ORM using MysqlAlchemy'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_engine

Base = declarative_base()


class State(Base):
    ''' Inherits from declarative_base and Defines a model'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
