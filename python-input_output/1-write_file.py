#!/usr/bin/python3
"""cunata cantidad de caracteres de una cadena"""


def write_file(filename="", text=""):
    """devuelve el numero de caracteres"""
    with open(filename, 'w', encoding='utf-8') as my_first_file:
        numero_caracteres = my_first_file.write(text)
        return numero_caracteres
