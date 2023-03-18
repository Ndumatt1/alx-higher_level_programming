#!/usr/bin/python3
''' This module defines an ORM using MysqlAlchemy'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
url = 'mysql://localhost:matthewlinux@3306'
Base = declarative_base()
class State(Base):
    ''' Defines a model'''
    __tablename__ = 'tables'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
