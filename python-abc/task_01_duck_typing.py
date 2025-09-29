#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return self.__radius**2 * pi

    def perimeter(self):
        return abs(self.__radius * 2 * pi)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return abs((self.__width + self.__height) * 2)


def shape_info(any_shape):
    print(f"Area: {any_shape.area()}")
    print(f"Perimeter: {any_shape.perimeter()}")
