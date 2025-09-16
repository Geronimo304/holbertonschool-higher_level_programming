#!/usr/bin/python3
"""creo la clase."""


class Square:
    """clase que representa un cuadrado."""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Decuelve el area del cuadrado"""
        return self.__size

    @size.setter
    def size(self, value):
        """le asigna valor a size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """devuelve el area del cuadrado"""
        return self.__size ** 2
