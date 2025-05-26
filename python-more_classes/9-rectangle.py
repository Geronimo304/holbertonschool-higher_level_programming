#!/usr/bin/python3
"""Clase Rectangle que define un rectángulo y permite crear cuadrados."""


class Rectangle:
    """Define un rectángulo con ancho y alto, atributos de clase y métodos."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inicializa el rectángulo con ancho y alto opcionales."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Devuelve el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho del rectángulo con validación."""
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
        """Establece el alto del rectángulo con validación."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.width * self.height

    def perimeter(self):
        """Devuelve el perímetro del rectángulo."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Devuelve la representación en cadena del rectángulo usando print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        line = str(self.print_symbol) * self.width
        rect_lines = [line for _ in range(self.height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Devuelve la representación oficial del rectángulo para recrearlo."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Mensaje al borrar una instancia y decrementa el contador."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Devuelve el rectángulo con mayor área o rect_1 si son iguales.

        Args:
            rect_1 (Rectangle): Primer rectángulo.
            rect_2 (Rectangle): Segundo rectángulo.

        Raises:
            TypeError: Si rect_1 o rect_2 no son instancias
            de Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Devuelve un nuevo rectángulo con ancho y alto iguales a size."""
        return cls(size, size)
