#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in my_list:
            if x is not count:
                print("{}".format(item), end="")
                count += 1
        print()
    except Exception:
        pass
    return count
