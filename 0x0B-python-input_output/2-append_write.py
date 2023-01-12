#!/usr/bin/python3
""" This module appends a string at the end of a text file. """


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file.
    Parameter:
    filename - name of file
    text - string to be added to file
    """
    with open(filename, "a", encoding="utf-8") as file:
        characters = file.write(text)
    return characters
