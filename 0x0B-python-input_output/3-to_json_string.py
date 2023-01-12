#!/usr/bin/python3
""" This module returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """ Returns the JSON representation of an object
    Parameters:
    my_obj - object to return.
    """
    json_object = json.dumps(my_obj)
    return json_object
