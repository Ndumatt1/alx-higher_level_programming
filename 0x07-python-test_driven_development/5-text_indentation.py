#!/usr/bin/python3
""" This module prints text with 2 new lines after ., ? and : """


def text_indentation(text):
    """ prints a text with 2 new lines after each ., ? and : """
    if type(text) != str:
        raise TypeError('text must be a string')
    text = text.replace(". ", ".\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(": ", ":\n\n")
    print("{}".format(text))
