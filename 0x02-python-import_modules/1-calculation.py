#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    result = a + b
    add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))

    a = 10
    b = 5
    result = a - b
    sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, result))

    a = 10
    b = 5
    result = a * b
    mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, result))

    a = 10
    b = 5
    result = a / b
    div(a, b)
    print("{:d} / {:d} = {:.0f}".format(a, b, result))
