#!/usr/bin/python3
""" This module defines a class Student. """


class Student:
    """ defines a student by:
    Instance attributes:
    firstname
    last_name
    age

    Methods:
    to_json - retrieves a dictionary representation of a student instance
    """
    def __init__(self, first_name, last_name, age):
        """ Instantiatses public instance attributes. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance"""
        return self.__dict__
