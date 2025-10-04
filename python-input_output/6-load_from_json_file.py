#!/usr/bin/python3
"""Defino la funcion"""


import json


def load_from_json_file(filename):
    """retrurn"""
    with open(filename, "r", encoding="utf-8") as archivo:
        return json.load(archivo)
