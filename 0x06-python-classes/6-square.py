#!/usr/bin/python3
""" This module defines a square. """


class Square:
    """ Defines a square. """
    def __init__(self, size=0, position=(0, 0)):
        """ Instantiate private instance size and private instance
        position. """
        self.__size = size
        self.__position = position
        if int(size) is not size:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """ getter function to retrieve size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function to set the value of size. """
        self.__size = value

    @property
    def position(self):
        """ getter function to retrieve position. """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter function to set the value of position. """
        self.__position = value

    def area(self):
        """ public instance that returns the current square area. """
        return self.size ** 2

    def my_print(self):
        """ prints to stdout the square with the character # """
        num = self.__size
        pos = self.__position
        if num == 0:
            print()
        else:
            for i in range(pos[1]):
                print('')
            for i in range(num):
                for j in range(num):
                    print("#", end='')
                print()
