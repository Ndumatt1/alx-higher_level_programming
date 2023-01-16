#!/usr/bin/python3
""" This module creates a class Rectangle that inherits from Base. """
from models.base import Base


class Rectangle(Base):
    """ creates class Rectangle that inherits from base. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor for class Rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        elif self.__width <= 0:
            raise ValueError('width must be > 0')
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        elif self.__height <= 0:
            raise ValueError('height must be > 0')
        if not isinstance(self.__x, int):
            raise TypeError('x must be an integer')
        elif self.__x < 0:
            raise ValueError('x must be >= 0')
        if not isinstance(self.__y, int):
            raise TypeError('y must be an integer')
        elif self.__y < 0:
            raise ValueError('y must >= 0')
        super().__init__(id)

    @property
    def width(self):
        """ getter function to return the value of width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter function to set the value of width. """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ getter function to return the value of height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter function to set the value of height. """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ getter function to return the value of x. """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter function to set the value of x. """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ getter function to return the value of y. """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter function to set the value of y"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must >= 0')
        self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character '#' """
        for y in range(self.__y):
            print()
        for height in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            print("#" * self.__width)

    def __str__(self):
        """ str method. """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ assigns argument to each attribute in argument order. """
        index = 0
        if args:
            while index < len(args):
                if index == 0:
                    self.id = args[index]
                if index == 1:
                    self.__width = args[index]
                if index == 2:
                    self.__height = args[index]
                if index == 3:
                    self.__x = args[index]
                if index == 4:
                    self.__y = args[index]
                index += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.__id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """ returns dictionasry representation of a Rectangle"""
        id = self.id
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        s = {'id': id, 'width': width, 'height': height, 'x': x, 'y': y}
        return s
