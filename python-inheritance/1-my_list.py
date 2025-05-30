#!/usr/bin/python3
"""Clase MyList que hereda list"""


class MyList(list):
    """Imprime la lista sin modificar nada"""
    def print_sorted(self):
        print(sorted(self))
