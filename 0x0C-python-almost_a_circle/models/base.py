#!/usr/bin/python3
""" This module creates a class Base. """


class Base:
    """ Base class for all other classes in the object. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor to instatiate public instance id. """
        if id is None:
            Base.__nb_objects += 1 
            self.id = Base.__nb_objects
        else:
            self.id = id
