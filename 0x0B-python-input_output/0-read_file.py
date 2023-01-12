#!/usr/bin/python3
""" This module reads a text file (UTF8) and prints to stdout ."""


def read_file(filename=""):
    """ Reads a text file and prints to stdout"""
    with open(filename, "r", encoding="utf-8") as file:
        read = file.read()
    print(read)
