#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = list(a_dictionary.keys())
    key.sort()
    for keys in key:
        print("{:s}: {}".format(keys, a_dictionary[keys]))
        
