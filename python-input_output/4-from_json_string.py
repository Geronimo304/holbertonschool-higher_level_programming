#!/usr/bin/python3
"""convierte una cadena JSON a un objeto python"""
import json


def from_json_string(my_str):
    """cadena JSON a un objeto python"""
    return json.loads(my_str)
