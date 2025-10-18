#!/usr/bin/env python3
"""
Módulo básico de serialización y deserialización con JSON.

Este módulo permite:
- Guardar un diccionario de Python como archivo JSON.
- Cargar un archivo JSON y convertirlo nuevamente en un diccionario de Python.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializa un diccionario de Python y lo guarda en un archivo JSON.

    Args:
        data (dict): Diccionario con los datos a serializar.
        filename (str): Nombre del archivo JSON donde se guardarán los datos.

    Si el archivo ya existe, será reemplazado.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Carga y deserializa un archivo JSON, convirtiéndolo en un diccionario de Python.

    Args:
        filename (str): Nombre del archivo JSON a leer.

    Returns:
        dict: Diccionario con los datos deserializados.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
