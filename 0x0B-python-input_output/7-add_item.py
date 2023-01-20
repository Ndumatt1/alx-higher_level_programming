#!/usr/bin/python3
""" This module adds all arguments to python list,
and then save them to a file
"""
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def run():    
    """ Stores the arguments"""
    del argv[0]
    try:
        args = load_from_json_file('add_item.json')
    except FileNotFoundError:
        args = []
    args += argv
    save_to_json_file(args, 'add_item.json')


if __name__  == '__main__':
    run()
