#!/usr/bin/python3
"""Define una clase Rectangle (Rectángulo)"""


class Rectangle:
    """Representa un rectángulo"""

    def __init__(self, width=0, height=0):
        """
        Constructor de la clase.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Método para obtener (leer) el valor del ancho"""
        return self.__width

    @width.setter
    def width(self, value):
        """Método para establecer (modificar) el valor del ancho con validación:"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Método para obtener (leer) el valor del alto"""
        return self.__height

    @height.setter
    def height(self, value):
        """Método para establecer (modificar) el valor del alto con validación."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Devuelve el área del rectángulo.
        Fórmula: ancho * alto
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Devuelve el perímetro del rectángulo.
        Fórmula: 2 * (ancho + alto)
        Si el ancho o el alto son 0, el perímetro es 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
