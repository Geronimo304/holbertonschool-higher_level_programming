#!/usr/bin/python3
"""define una clase rectangle."""

class   Rectangle:
    """representa un rectangulo"""

    def __init__(self, ancho=0, alto=0):
       
       self.establecer_ancho(ancho)
       self.establecer_alto(alto)

    def obtener_ancho(self):
        """decuelve el ancho"""
        return self.__ancho
    
    def establecer_ancho(self, valor):
        if not isinstance(valor, int):
            raise TypeError("width must be an integer")
        if valor < 0:
            raise ValueError("width must be >= 0")
        self.__ancho = valor

    def obtener_alto(self):
        """devuelve el alto"""
        return self.__alto

    def establecer_alto(self, valor):
        if not isinstance(valor, int):
            raise TypeError("height must be an integer")
        if valor < 0:
            raise ValueError("height must be >= 0")
        self.__alto = valor
