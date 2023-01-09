#!/usdr/bin/python3
""" This module returns the list of available attributes of an object. """


def lookup(obj):
    """ Returns the list of available attributes and method of an object.
    obj - object to return
    """
    list = dir(obj)
    return list
