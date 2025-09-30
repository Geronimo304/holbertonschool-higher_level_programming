#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as archivo:
        archivo_completo = archivo.read()
        print(archivo_completo, end="")
