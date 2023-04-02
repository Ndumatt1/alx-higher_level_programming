#!/usr/bin/python3
'''
This module finds a peak in a list of unsorted integer
'''


def find_peak(list_of_integer):
    ''' Finds a peak in a list of unsorted integer '''
    value = list_of_integer
    if value == []:
        return None
    if len(value) == 1:
        return None
    for i in range(len(value) - 1):
        if value[i] >= value[i + 1] and value[i] >= value[i - 1]:
            return value[i]
