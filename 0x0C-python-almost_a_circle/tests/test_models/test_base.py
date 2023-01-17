#!/usr/bin/python3
""" This module contains unittest testing for Base class. """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class test_base(unittest.TestCase):
    """ inherits from unittest Tescases to use the unittest modules"""
    def test_assign_automatic(self):
        """ test to check for automatic assignment of id"""
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id_not_None(self):
        """ checks if id is not None"""
        base = Base(10)
        self.assertEqual(base.id, 10)
