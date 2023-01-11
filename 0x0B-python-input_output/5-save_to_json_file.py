#!/usr/bin/python3
""" This module writes an object to a text file, Using JSON
representattion
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to text file.
    Parameters:
    my_obj - object to write.
    filename - file to write to
    """
    with open(filename, "w", encoding="utf-8") as file:
        return json.dump(my_obj, file)
