#!/usr/bin/python3
""" Defines a square """


class Square:
    """ This defines a square. """
    def __init__(self, size=0):
        """ Instantiate private instance attribute """
        self.__size = size
        if int(size) is not size:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be an integer')

    def area(self):
        """ Returns the current squasre area """
        return self.__size * self.__size
