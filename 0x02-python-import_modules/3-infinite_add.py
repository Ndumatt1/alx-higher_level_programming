#!/usr/bin/python3
if __name__ == '__main__':

    from sys import argv

    if len(argv) == 1:
        add = 0
    else:
        add = 0
        for i in range(1, len(argv)):
            num = int(argv[i])
            add += num
        print("{:d}".format(add))
