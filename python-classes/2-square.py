#!/usr/bin/python3
"""Defino la calse."""

class square:
    """Representa un cuadrado"""

    def __init__(self, size=0):
        """Inicializa una nueva instancia.
        
        Args:
            size (int): El tamaño del cuadrado (por defecto 0)
        """

        if not isinstance(size, int):
            raise TypeError("debe de ser un numero entero")
        if size < 0:
            raise ValueError("el tamaño debe de ser mayor a 0 ")
        self.__size = size
