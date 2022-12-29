#!/usr/bin/python3
""" This module defines a square. """


class Square:
    """ Defines a square. """
    def __init__(self, size=0):
        """ Instantiates private attribute. """
        self.__size = size
        if int(size) is not size:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
