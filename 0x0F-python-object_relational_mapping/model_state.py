#!/usr/bin/python3
''' This module defines an ORM using MysqlAlchemy'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    ''' Defines a model'''
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
