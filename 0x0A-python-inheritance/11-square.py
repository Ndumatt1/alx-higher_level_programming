#!/usr/bin/python3
""" Writes a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a class Square. """
    def __init__(self, size):
        """ Instatiation with size. """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns that area of the square"""
        return self.__size ** 2

    def __str__(self):
        """ string format"""
        return "[Square] {}/{}".format(self.__size, self.__size)
