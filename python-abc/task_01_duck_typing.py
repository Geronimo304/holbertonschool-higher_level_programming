#!/usr/bin/python3
"""
This module demonstrates abstract base classes and duck typing in Python.
It defines an abstract Shape class and concrete Circle and
Rectangle implementations.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class for shapes.
    Defines the interface that all shapes must implement.
    """
    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        Returns:
            float: The area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter (or circumference) of the shape.
        Returns:
            float: The perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Class representing a circle.
    Inherits from the Shape abstract class and implements the area
    and perimeter methods.
    """
    def __init__(self, radius):
        """
        Initialize a Circle with the given radius.
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        Returns:
            float: The area of the circle (π * (r^(2)))
        """
        return math.pi * (self.radius) ** 2

    def perimeter(self):
        """
        Calculate the circumference of the circle.
        Returns:
            float: The circumference of the circle (2 * π * r)
        """
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Class representing a rectangle.
    Inherits from the Shape abstract class and implements
    the area and perimeter methods.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle with the given width and height.
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            float: The area of the rectangle (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        Returns:
            float: The perimeter of the rectangle (2 * (width + height))
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    This function uses duck typing to handle any object that
    has area() and perimeter() methods, regardless of its actual class.
    This demonstrates how Python's duck typing works if it looks like a
    Shape and behaves like a Shape, we can treat it as a Shape.

    Args:
        shape: An object that has area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
