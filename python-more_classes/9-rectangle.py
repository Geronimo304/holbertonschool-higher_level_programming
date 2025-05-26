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
        """Obtiene el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho, asegurando que sea entero >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtiene el alto del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece el alto, asegurando que sea entero >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula el área del rectángulo."""
        return self.width * self.height

    def perimeter(self):
        """Calcula el perímetro del rectángulo."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Representación en cadena usando el símbolo print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        line = str(self.print_symbol) * self.width
        rect_lines = [line for _ in range(self.height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Representación que permite recrear la instancia con eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Mensaje al borrar instancia y decremento del contador."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Devuelve el rectángulo con área mayor o rect_1 si son iguales.

        Args:
            rect_1 (Rectangle): primer rectángulo.
            rect_2 (Rectangle): segundo rectángulo.

        Raises:
            TypeError: si rect_1 o rect_2 no son instancias de Rectangle.
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
        """Retorna un nuevo rectángulo con ancho y alto iguales a size."""
        return cls(size, size)
