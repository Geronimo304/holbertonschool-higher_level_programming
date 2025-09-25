#!/usr/bin/python3
""" Defino la class. """


class BaseGeometry:
    """Declaro la class basegeometry"""
    def area(self):
        """Devuelve exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Codeo las exepciones"""
        if type(value)is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError (f"{name} must be greater than 0")

"""Defino la clase rectangulo"""


class Rectangle:
    def __init__(self, width, height):
        """Comprobamos que sean enteros positivos"""
        if type(width) is not int:
            raise TypeError("height must be an integer")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        self.__height = height