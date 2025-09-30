#!/usr/bin/python3
"""defini la funcion"""


def write_file(filename="", text=""):
    """Cuento los caracteres del texto"""
    with open(filename, "w", encoding="utf-8") as texto:
        return texto.write(text)
