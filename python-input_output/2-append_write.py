#!/usr/bin/python3
"""añade una cadena al final y devuelve numero de caracteres"""


def append_write(filename="", text=""):
    """cadena al final y devuelve numero"""
    with open(filename, 'a', encoding="utf-8") as file_append:
        file_append.write(text)
        return len(text)
