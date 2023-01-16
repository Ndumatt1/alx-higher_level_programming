#!/usr/bin/python3
""" This modeule creates a class Square that inherits from Rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from class Rectangle. """
    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor. """
        self.__size = size
        self.__x = x
        self.__y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str method ."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.__size)

    @property
    def size(self):
        """ getter function. """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function. """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width muwt be > 0')
        self.__size = value

    def update(self, *args, **kwargs):
        """ assigns attributes.
        1st argument should be id attribute
        2nd argument should be size attribute
        3rd argument should be x attribute
        4th argument should be y attribute
        """
        if args and args is not None:
            index = 0
            while index < len(args):
                if index == 0:
                    self.__id = args[index]
                if index == 1:
                    self.__size = args[index]
                if index == 2:
                    self.__x = args[index]
                if index == 3:
                    self.__y = args[index]
                index += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.__id = value
                if key == 'size':
                    self.__size = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """ Returns the dictionary representattion of a Square. """
        id = self.id
        size = self.__size
        x = self.__x
        y = self.__y
        obj = {'id': id, 'size': size, 'x': x, 'y': y}
        return obj
