def print_list_integer(my_list=[]):
    if my_list == 0:
        my_list = []
    else:
        for i in my_list:
            print("{:d}".format(i))
