#!/usr/bin/python3
"""Defino la funcion"""


def read_file(filename=""):
    """Lee un archivo con estandar utf-8"""
    with open(filename, "r", encoding="utf-8") as archivo:
        archivo_completo = archivo.read()
        print(archivo_completo, end="")
