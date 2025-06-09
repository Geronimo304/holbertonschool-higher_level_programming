#!/usr/bin/python3
"""objeto a partir de un archivo JSON"""
import json


def load_from_json_file(filename):
    """crea un objeto"""
    with open(filename, 'r') as my_fake:
        objeto = json.load(my_fake)
        return objeto
