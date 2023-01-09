#!/usr/bin/python3
""" This module write a class that inherits from list"""


class MyList(list):
    """ A class that inherits from list. """
    def print_sorted(self):
        """ prints the sorted list in ascending sort. """
        sorted_list = sorted(self)
        print("{}".format(sorted_list))
