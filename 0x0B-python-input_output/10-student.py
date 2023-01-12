#!/usr/bin/python3
""" This module defines a class Student. """


class Student:
    """ Defines a class Student. """
    def __init__(self, first_name, last_name, age):
        """ Instantiates public attributes. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a student instance"""
        json_obj = {}
        if attrs is None:
            return self.__dict__
        else:
            for attr in attrs:
                if hasattr(self, attr):
                    json_obj[attr] = getattr(self, attr)
            return json_obj
