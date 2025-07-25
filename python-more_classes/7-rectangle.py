#!/usr/bin/python3
"""Define la clase Rectángulo con símbolo de impresión personalizable."""


class Rectangle:
    """Representa un rectángulo."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inicializa una nueva instancia de Rectángulo."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Devuelve el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho del rectángulo."""
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
        """Establece el alto del rectángulo."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcula el perímetro del rectángulo.

        Si el ancho o el alto es 0, el perímetro es 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Devuelve la representación con el símbolo de impresión.

        Usa print_symbol para construir la forma.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        line = str(self.print_symbol) * self.__width
        rect_lines = [line for _ in range(self.__height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Devuelve una cadena para recrear la instancia usando eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Mensaje y actualización al eliminar una instancia."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
