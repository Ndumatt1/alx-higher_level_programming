#!/usr/bin/python3
""" This module divides 2 integers and prints the result"""


def safe_print_division(a, b):
    """ Divides 2 integers and print the result"""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
