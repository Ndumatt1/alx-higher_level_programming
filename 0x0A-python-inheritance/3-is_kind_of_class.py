#!/usr/bin/python3
""" This module checks if an object is an instance of a class
or object of an instance of a class that inherited from the specific class.
"""


def is_kind_of_class(obj, a_class):
    """ Returns True is the object is an instance of, or is the object
    is an instance of a class that inherited from, the specified class
    otherwise False
    """
    return isinstance(obj, a_class)
