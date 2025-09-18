#!/usr/bin/python3
"""creo la clase."""


class Square:
    """clase que representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    
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

    @property
    def position(self):
        """devuelve la posicion del cuadrado"""
        return self.__position

    @position.setter
    def position(self, value):
        """verifica la tupla"""
        if (
            not isinstance(value, tuple)
        or len(value) != 2
        or not all(isinstance(num, int) for num in value)
        or not all(num >= 0 for num in value)
        ):
            raise TypeError("size must be an integer")
        self.__position = value
    
    def area(self):
        """devuelve el area del cuadrado"""
        return self.__size ** 2

    def my_print(self):
        """imprime el cuadrado"""
        if self.__size == 0:
            print()
            return

        if self.__position[1] > 0:
            print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
