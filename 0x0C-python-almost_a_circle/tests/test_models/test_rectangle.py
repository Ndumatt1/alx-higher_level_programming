#!/usr/bin/python3
""" This module contains unittest test for Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import sys
import io


class test_rectangle(unittest.TestCase):
    """ inherits from unittest TestCase. """

    def test_rectangle(self):
        """ test rectangle. """
        rect = Rectangle(1, 2)
        rect1 = Rectangle(1, 2, 3)
        rect2 = Rectangle(1, 2, 3, 4)
        rect3 = Rectangle(1, 2, 3, 4, 5)
        """ test for when attributes of Rectangle is not int. """
        with self.assertRaises(TypeError):
            rect4 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            rect5 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            rect6 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            rect7 = Rectangle(1, 2, 3, "4")
        """ test for when attributes of Rectangle is less than 0"""
        with self.assertRaises(ValueError):
            rect8 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            rect9 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            rect10 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            rect11 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            rect12 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            rect13 = Rectangle(1, 2, 3, -4)
    def test_area(self):
        """ tests for the area of the triangle."""
        rect = Rectangle(3, 3)
        rect1 = Rectangle(4, 5)
        self.assertEqual(rect.area(), 9)
        self.assertEqual(rect1.area(), 20)

    def test_output(self):
        """ tests that the output is the same with the expected output."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rect = Rectangle(3, 4)
        rect.display()
        sys.stdout = sys.__stdout__
        expected_output = ("#" * rect.width+ '\n') * rect.height
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str(self):
        """ test for the magic method __str__"""
        output = "[Rectangle] (12) 2/1 - 4/5"
        rect = Rectangle(4, 5, 2, 1, 12)
        self.assertEqual(str(rect), output)
