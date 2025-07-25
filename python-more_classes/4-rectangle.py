#!/usr/bin/python3
"""Define una clase Rectángulo."""


class Rectangle:
    """Representa un rectángulo."""

    def __init__(self, width=0, height=0):
        """Inicializa una nueva instancia de Rectángulo.

        Args:
            width (int): Ancho del rectángulo (por defecto 0).
            height (int): Alto del rectángulo (por defecto 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Devuelve el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho del rectángulo.

        Args:
            value (int): Nuevo valor para el ancho.

        Lanza:
            TypeError: Si el valor no es un entero.
            ValueError: Si el valor es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Devuelve el alto del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece el alto del rectángulo.

        Args:
            value (int): Nuevo valor para el alto.

        Lanza:
            TypeError: Si el valor no es un entero.
            ValueError: Si el valor es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Devuelve el perímetro del rectángulo.

        Si el ancho o alto es 0, devuelve 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Devuelve una representación con # del rectángulo para imprimir."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Devuelve una cadena para recrear la instancia usando eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
