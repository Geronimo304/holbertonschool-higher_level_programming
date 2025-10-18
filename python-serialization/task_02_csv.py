#!/usr/bin/python3
"""
Convierte un archivo CSV a formato JSON llamado 'data.json'.
Cada fila del CSV se transforma en un diccionario usando los encabezados.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convierte un CSV a JSON.

    Args:
        filename (str): Ruta del archivo CSV.

    Returns:
        bool: True si la conversión fue exitosa, False si hubo un error.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = list(csv.DictReader(f))

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Archivo '{filename}' no encontrado.")
        return False
    except Exception as e:
        print(f"Error durante la conversión: {e}")
        return False
