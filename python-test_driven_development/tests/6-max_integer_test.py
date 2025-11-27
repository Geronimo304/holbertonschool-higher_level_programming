#!/usr/bin/python3
"""task6 module"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([1, 2, -3]), 2)
        self.assertEqual(max_integer([5, 4]), 5)
        self.assertEqual(max_integer([3, 5, 2]), 5)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([]), None)
