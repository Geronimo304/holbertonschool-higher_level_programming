#!/usr/bin/python3
"""importo basegeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """clase Rectangle que hereda de basegeometrt"""

    def __init__(self, width, height):
        """valido width y height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Retorno la descripcion del rectangulo"""
        f"[Rectangle] {self.__width:d}/{self.__height:d}"

    
    def area(self):
        """Retorno el area del rectangulo"""
        return self.__width * self.__height
