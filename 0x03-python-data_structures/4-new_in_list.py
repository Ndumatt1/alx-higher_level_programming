#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0 or idx > len(my_list):
        return new_list
    else:
        for index in range(len(my_list)):
            if index == idx:
                new_list[index] = element
        return new_list
