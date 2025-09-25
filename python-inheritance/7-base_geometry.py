#!/usr/bin/python3
""" Defino la class. """


class BaseGeometry:
    """Declaro la class basegeometry"""
    def area(self):
        """Devuelve exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Codeo las exepciones"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError ("<name> must be greater than 0")
