#!/usr/bin/python3
"""Define una clase Rectangle."""


class Rectangle:
    """Representa un rectángulo."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Devuelve el ancho."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho, validando tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Devuelve el alto."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece el alto, validando tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
