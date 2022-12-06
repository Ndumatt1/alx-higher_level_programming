#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
         return None
    else:
        res = my_list[0]
        for index in my_list:
            if index > res:
                res = index
        return res

