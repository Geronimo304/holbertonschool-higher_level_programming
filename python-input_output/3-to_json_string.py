#!/usr/bin/python3
"""funcion que devuelve la representacion JSON"""
import json


def to_json_string(my_obj):
    """devuelve representacion JSON"""
    return json.dumps(my_obj)
