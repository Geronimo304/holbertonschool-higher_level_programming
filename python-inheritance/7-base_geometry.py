#!/usr/bin/python3
"""
Module that defines the BaseGeometry class.
This module provides a base class for geometry-related classes.
"""


class BaseGeometry:
    """
    BaseGeometry class with area method.
    This class serves as a base for geometry-related classes.
    """
    def area(self):
        """
        Calculates the area of a geometric shape.
        This method must be implemented by derived classes.

        Raises:
            Exception: Always raises an Exception with the message
                      'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.
        Args:
            name (str): The name of the value being validated
            value: The value to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
