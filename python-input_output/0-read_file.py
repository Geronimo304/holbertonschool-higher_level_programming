#!/usr/bin/python3
"""inicializo la funcion"""


def read_file(filename=""):
    """abro el archivo y lo lee"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
