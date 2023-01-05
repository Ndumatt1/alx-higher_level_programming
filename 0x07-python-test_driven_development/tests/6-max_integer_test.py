#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_emptylist(self):
        self.assertEqual(max_integer([]), None)
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_float_in_list(self):
        self.assertEqual(max_integer([3.5, 8.9, 9.8, 1.1]), 9.8)
    def test_negative_in_list(self):
        self.assertEqual(max_integer([-1, -3, -6, -3]), -1)
        
