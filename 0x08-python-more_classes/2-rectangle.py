#!/usr/bin/python3
""" This module writes a class Rectangle that defines a rectangle. """


class Rectangle:
    """ writes a class Rectangle that defines a rectangle. """
    def __init__(self, width=0, height=0):
        """ Instantiates private instance attribute width and height. """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter function to retrieve private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter function to set the value of width. """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ getter function to retrieve the value of height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter function to set the value of height. """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns the rectangle area. """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the rectangle perimeter. """
        return 2 * (self.__width + self.__height)
