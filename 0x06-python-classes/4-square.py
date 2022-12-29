#!/usr/bin/python3
""" Defines a square. """


class Square:
    """ Defines a square. """
    def __init__(self, size=0):
        """ Instantiates private instance. """
        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """ getter method to retrieve private instance """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method to set private instance. """
        self.__size = value

    def area(self):
        """ returns current square area """
        return self.__size * self.__size
