#!/usr/bin/python3
"""
This module defines a class LockedClass that prevents user from
dynamically creating a new instance attribute except if the new instance
attribute is called first_name
"""


class LockedClass:
    """ defines class LockedClass. """
    __slots__ = ("first_name")

    def __init__(self, first_name=""):
        """ sets attribute to first_name. """
        self.first_name = first_name
