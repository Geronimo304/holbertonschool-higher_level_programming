#!/usr/bin/python3
"""defino la funcion"""


import json


def from_json_string(my_str):
    """retorno un json transformado a objeto"""
    return json.loads(my_str)
