#!/usr/bin/python3
"""definio la funcion"""


import json


def save_to_json_file(my_obj, filename):
    """retorno"""
    with open(filename, "w") as archivo:
        return archivo.write(json.dumps(my_obj))
