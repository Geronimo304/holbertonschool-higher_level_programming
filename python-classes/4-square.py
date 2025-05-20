#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa un cuadrado con un tamaño opcional."""
        self.size = size  # Usa el setter para validar

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado con validación."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2
