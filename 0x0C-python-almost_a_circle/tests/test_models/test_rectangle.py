#!/usr/bin/python3
""" This module contains unittest test for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """ inherits from unittest TestCase. """

    def test_width(self):
        """ test for width. """
        rect1 = Rectangle(10, 12)
        self.assertEqual(rect1.width, 10)

    def test_width_setter(self):
        """ test for width setter"""
        rect1 = Rectangle(10, 10)
        rect1.width = 12
        self.assertEqual(rect1.width, 12)

    def test_width_error(self):
        """ tests for exception when width is not an integer. """
        rect1 = Rectangle(2, 10)
        with self.assertRaises(TypeError):
            rect1.width = 'uche'

    def test_width_error(self):
        """ tests for exception when width is equal to 0"""
        rect1 = Rectangle(2, 10)
        with self.assertRaises(ValueError):
            rect1.width = 0

    def test_width_error(self):
        """ test for exception when width is less than 0"""
        rect = Rectangle(10, 10)
        with self.assertRaises(ValueError):
            rect.width = -1

    def test_height(self):
        """ test for height. """
        rect = Rectangle(2, 1)
        self.assertEqual(rect.height, 1)

    def test_height_setter(self):
        """ test for height getter """
        rect = Rectangle(2, 8)
        rect.height = 10
        self.assertEqual(rect.height, 10)

    def test_height_exception(self):
        """ test for height exception. """
        rect = Rectangle(10, 10)
        with self.assertRaises(TypeError):
            rect.height = 'School'

    def test_height_ValueError(self):
        """ test for when height is equal to 0"""
        rect = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_height_less_than_zero(self):
        """ test for when height is less than 0"""
        rect = Rectangle(2, 4)
        with self.assertRaises(ValueError):
            rect.height = -1

    def test_x(self):
        """ test for x with optional instantiation. """
        rect = Rectangle(10, 12)
        self.assertEqual(rect.x, 0)

    def test_x_argument(self):
        """ test for x when given a argument"""
        rect = Rectangle(10, 2, 9)
        self.assertEqual(rect.x, 9)

    def test_x_setter(self):
        """ test for x setter and getter """
        rect = Rectangle(10, 10)
        rect.x = 12
        self.assertEqual(rect.x, 12)

    def text_x_exception(self):
        """ test if x raises expected exception when x is not an integer"""
        rect = Rectangle(10, 10)
        with self.assertRaises(TypeError):
            rect.x = 'my'

    def test_x_under_zero(self):
        """ test for when x is less than zero"""
        rect = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            rect.x = -9

    def test_y_value(self):
        """ test for y"""
        rect = Rectangle(1, 3, 7)
        self.assertEqual(rect.y, 0)

    def test_t_argument(self):
        """ test for y when passed as an argument. """
        rect = Rectangle(1, 2, 3, 8)
        self.assertEqual(rect.y, 8)

    def test_y_setter(self):
        """ test for y value when assigned with setter. """
        rect = Rectangle(1, 2, 3)
        rect.y = 9
        self.assertEqual(rect.y, 9)

    def test_y_exception(self):
        """ test for when y is not an integer. """
        rect = Rectangle(1, 2, 4)
        with self.assertRaises(TypeError):
            rect.y = 'my'

    def test_y_ValueError(self):
        """ test for when y is less than 0"""
        rect = Rectangle(1, 4, 8)
        with self.assertRaises(ValueError):
            rect.y = -2
