#!/usr/bin/python3
"""This module writes a class BaseGeometry. """


class BaseGeometry:
    """ Defines a class. """

    def area(self):
        """ raises an Exception. """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value. """
        self.name = name
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(self.name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))
        self.value = value


class Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Instantiate width and height"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ str method to print out string. """    
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ returns the area of the rectangle. """
        return self.__width * self.__height
