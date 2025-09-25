#!/usr/bin/python3
""" Defino la class. """


class BaseGeometry:
    """Declaro la class basegeometry"""
    def area(self):
        """Devuelve exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Codeo las exepciones"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""Defino la clase rectangulo"""


class Rectangle(BaseGeometry):
    """Declaro la class rectangle heredada de basegeometry"""
    def __init__(self, width, height):
        """Comprobamos que sean enteros positivos"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
