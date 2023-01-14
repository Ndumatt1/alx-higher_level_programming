#!/usr/bin/python3
""" This module creates a class Rectangle that inherits from Base. """
from models.base import Base


class Rectangle(Base):
    """ creates class Rectangle that inherits from base. """    
        
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor for class Rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """ getter function to return the value of width. """
            return self.__width

        @width.setter
        def width(self, value):
           """ setter function to set the value of width. """
           self.__width = value

        @property
        def height(self):
            """ getter function to return the value of height. """
            return self.__height

        @height.setter
        def height(self, value):
            """ setter function to set the value of height. """
            self.__height = value

        @property
        def x(self):
            """ getter function to return the value of x. """
            return self.__x

        @x.setter
        def height(self, value):
            """ setter function to set the value of x. """
            self.__x = value

        @property
        def y(self):
            """ getter function to return the value of y. """
            return self.__y

        @y.setter
        def y(self, value):
            """ setter function to set the value of y"""
            self.__y = value
