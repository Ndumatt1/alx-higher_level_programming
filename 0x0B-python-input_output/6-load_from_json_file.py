#!/usr/bin/python3
""" This module creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """ Creates an object from a JSON file.
    Parameters:
    filename - Name of file """
    with open(filename, "r", encoding="utf-8") as file:
        json_object = json.load(file)
