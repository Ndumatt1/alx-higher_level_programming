#!/usr/bin/python3

for number in range(0, 100):

    if number -1:
        sep = ", "

    print("{:02d}{}".format(number, sep), end="")
