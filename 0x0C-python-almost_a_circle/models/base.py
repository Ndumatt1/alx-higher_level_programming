#!/usr/bin/python3
""" This module creates a class Base. """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns JSON string representation of list_dictionary. """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file. """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string."""
        if json_string is None or json_string == []:
            return json_string
        else:
            return json.loads(json_string)
