#!/usr/bin/python3
"""
Module that defines the Rectangle class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            int: The area (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.
        Returns:
            str: String in the format [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
