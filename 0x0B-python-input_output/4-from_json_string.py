#!/usr/bin/python3
""" This module returns an object (Python data structure)
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON string.
    Parameters:
    my_string - string to return
    """
    return json.loads(my_str)
