#!/usr/bin/python3
"""Define a class Rectangle that supports printing and recreation."""

class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string of the rectangle with '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        rect_lines = []
        for _ in range(self.height):
            rect_lines.append("#" * self.width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Return a string that can recreate the rectangle using eval()."""
        return f"Rectangle({self.width}, {self.height})"
