#!/usr/bin/python3
"""inisializamos la class"""


class Square:
    def __init__(self, size = 0):
        if not isinstance (size, int):
            TypeError("size must be an integer")
        if size < 0:
            ValueError("size must be >= 0")
        self.__size = size
