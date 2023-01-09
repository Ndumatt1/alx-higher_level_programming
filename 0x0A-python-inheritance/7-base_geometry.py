#!/usr/bin/python3
""" This module writes a class BaseGeometry. """


class BaseGeometry:
    """ Defines a class. """

    def area(self):
        """ raises an Exception. """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value. """
        assert isinstance(name, str)
        self.name = name
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(self.name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))
        self.value = value
