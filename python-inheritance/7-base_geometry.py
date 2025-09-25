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
