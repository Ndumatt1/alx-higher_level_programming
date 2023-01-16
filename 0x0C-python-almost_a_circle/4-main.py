#!/usr/bin/python3
from models.rectangle import Rectangle

if __name__ == '__main__':
    r1 = Rectangle(4, 2)
    r1.display()
    print('---')

    r1 = Rectangle('uche', 3)
    r1.display()
