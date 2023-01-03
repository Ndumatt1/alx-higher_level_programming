#!/usr/bin/python3
"""This module defines a rectangle. """


class Rectangle:
    """defines a rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Instantiates private attribute width and height. """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter function to return the value of width. """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter function to set the value of width. """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ getter function to return the value of height. """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter function to set the value of height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter. """
        if self.width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ str method to print the rectangle with  character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        s = ""
        for row in range(self.__height):
            for col in range(self.__width):
                s += "#"
            if (row + 1) is not self.height:
                s += "\n"
        return s

    def __repr__(self):
        """ returns the string representation of the triangle. """
        return f"Rectangle({self.__width},{self.__height})"

    def __del__(self):
        """ Deletes an instance of a rectangle. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
