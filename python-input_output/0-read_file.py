#!/usr/bin/python3
"""archivo de texto UTF-8 y lo imprime en stdout"""


def read_file(filename=""):
    """funcio para leer un archivo"""
    with open(filename, 'r', encoding='utf-8') as my_file_0:
        for linea in my_file_0:
            print(linea, end='')
