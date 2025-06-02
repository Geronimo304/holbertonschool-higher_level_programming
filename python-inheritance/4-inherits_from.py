#!/usr/bin/python3
"""
This module provides a function that determines whether an object
is an instance of a subclass (direct or indirect) of a specified class,
excluding instances of the class itself.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a subclass of a_class.

    This function returns True if obj is an instance of a class that
    inherited (directly or indirectly) from a_class, but not if it is
    an instance of a_class itself.

    Args:
        obj: The object to check.
        a_class: The class to compare inheritance against.

    Returns:
        True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
