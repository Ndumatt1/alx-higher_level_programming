#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    unique_numbers = set(my_list)
    for index in unique_numbers:
        total += index
    return total
