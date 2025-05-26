#!/usr/bin/python3
"""Define una clase Rectangle (Rectángulo)"""


class Rectangle:
    """Representa un rectángulo"""

    def __init__(self, width=0, height=0):
        """
        Constructor de la clase.
        Permite crear un rectángulo con ancho y alto opcionales
        (por defecto 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Método para obtener (leer) el valor del ancho"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Método para establecer (modificar) el valor del ancho con validación:
        - Debe ser un entero, si no lanza TypeError.
        - Debe ser >= 0, si no lanza ValueError.
        """
        if not isinstance(value, int):
            raise TypeError(
                "width must be an integer")
        if value < 0:
            raise ValueError(
                "width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Método para obtener (leer) el valor del alto"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Método para establecer (modificar) el valor del alto con validación:
        - Debe ser un entero, si no lanza TypeError.
        - Debe ser >= 0, si no lanza ValueError.
        """
        if not isinstance(value, int):
            raise TypeError(
                "height must be an integer")
        if value < 0:
            raise ValueError(
                "height must be >= 0")
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
        Si el ancho o el alto es 0, el perímetro es 0.
        Fórmula: 2 * (ancho + alto)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Devuelve una representación en string del rectángulo con `#`.
        Cada línea representa una fila del rectángulo.
        Si el ancho o alto es 0, devuelve una cadena vacía.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = []
        for _ in range(self.__height):
            rect_lines.append("#" * self.__width)
        return "\n".join(rect_lines)
