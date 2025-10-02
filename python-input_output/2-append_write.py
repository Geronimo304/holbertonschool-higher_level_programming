#!/usr/bin/python3
""" creo la funcion"""


def append_write(filename="", text=""):
    """Agrega una cadena al final de un archivo (UTF8)
    y devuelve el número de caracteres agregados
    """
    with open(filename, "a", encoding="utf-8") as archivo:
        return archivo.write(text)
