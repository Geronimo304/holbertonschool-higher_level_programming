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
        """establece el ancho del rectangulo, siempre en cuando sea entero"""
        
        if not isinstance(valor, int):
            raise TypeError("NO ES UN ENTERO")
        if valor < 0:
            raise ValueError("DEBE SER MAYOR A 0")
        self.__ancho = valor

    def obtener_alto(self):
        """Devuelve el alto"""
        return self.__alto
    
    def establecer_alto(self, valor):
        """establece el alto del rectangulo, siempre en cuando sea entero"""

        if not isinstance(valor, int):
            raise TypeError("NO ES ENTERO")
        if valor < 0:
            raise ValueError("ES MENOR A 0")
        self.__alto = valor
        