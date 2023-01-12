#!/usr/bin/python3
""" This module returns the dictionary description with simple
data structure for JSON serialization of an object
"""
import json


def class_to_json(obj):
    """ Returns the dictionary description.
    Parameters:
    obj - an instance of a class to serialized. """
    obj = json.dumps(obj.__dict__)
    return obj
