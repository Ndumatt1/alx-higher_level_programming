#!/usr/bin/python3
from models.rectangle import Rectangle

if __name__ == '__main__':
    r1 = Rectangle(2, 3)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
