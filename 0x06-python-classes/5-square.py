#!/usr/bin/python3
""" Defines a square. """


class Square:
    """ defines a square """
    def __init__(self, size=0):
        """ instantiate private instance attribute """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """ getter function to retrieve private instance attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function to set private instance attribute value """
        self.__size = value
        if type(value) is not int:
            return TypeError("size must be an integer")

    def area(self):
        """ returns the current square of area """
        return self.__size * self.__size

    def my_print(self):
        """ prints to stdout the square with the character # """
        num = self.__size
        if num == 0:
            print()
        else:
            for i in range(num):
                for j in range(num):
                    print("#", end='')
                print()
