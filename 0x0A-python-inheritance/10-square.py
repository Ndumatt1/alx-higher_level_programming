#!/usr/bin/python3
""" This module writes a class Sqaure that inherits from Rectangle. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square inherited from Rectangle. """
    def __init__(self, size):
        """ Instantiates size. """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns area of a square"""
        return self.__size ** 2
