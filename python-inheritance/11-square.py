#!/usr/bin/python3
"""Inicializo la clase cuadrado"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """clase squeare que hereda de rectangle"""
    def __init__(self, size):
        """uso super para poder usar la logica de la clase padre"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Llama al __str__ de Rectangle y añade algo extra """
        base_str = super().__str__()
        return f"{base_str}"
