#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_values(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 12.4, 3, 4]), 12.4)
        self.assertAlmostEqual(max_integer([-15, -7, -2, -9]), -2)

    def test_empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)
