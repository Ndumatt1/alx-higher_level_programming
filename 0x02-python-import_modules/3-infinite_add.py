#!/usr/bin/python3
if __name__ == '__main__':

    from sys import argv

    number = len(argv)

    if number == 1:
        add = 0
    else:
        for i in range(1, number):
            add = 0
            num = int(argv[i])
            add += num
            print("{:d}".format(add))
