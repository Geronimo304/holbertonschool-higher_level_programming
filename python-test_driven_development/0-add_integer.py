#!/usr/bin/python3
"""
This module provides a function to add two integers or floats,
casting them to integers first.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.
    """

    if a is None or not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")

    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
