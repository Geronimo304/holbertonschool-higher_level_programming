#!/usr/bin/python3
"""Defino la clase Square."""


class Square:
    """Clase que representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado con un tamaño."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
