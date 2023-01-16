#!/usr/bin/python3
""" This module contains unittest testing for Base class. """
import unittest
from models.base import Base
from models.rectangle import Rectangle

class test_base(unittest.TestCase):
    """ inherits from unittest Tescases to use the unittest modules"""
    def test_id(self):
        """ check test case for id"""
        b1 = Base()
        self.assertEqual(3, b1.id)
