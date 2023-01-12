#!/usr/bin/python3
""" This module writes a string to a text file. """


def write_file(filename="", text=""):
    """ Writes a string to a text file
    Parameters:
    filename - name of text file
    text - string to write to file
    """
    with open(filename, "w", encoding='utf-8') as file:
        characters = file.write(text)
    return characters
