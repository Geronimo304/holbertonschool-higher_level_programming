#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa un nuevo cuadrado.

        Args:
            size (int): El tamaño del lado del cuadrado (por defecto 0).

        Raises:
            TypeError: Si size no es un entero.
            ValueError: Si size es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado actual."""
        return self.__size ** 2
