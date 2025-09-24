import os

for i in range(1, 13):  # del 1 al 12 inclusive
    filename = f"{i}-main.py"
    with open(filename, "w") as f:
        f.write("#!/usr/bin/python3\n")  # línea inicial opcional
        f.write(f"# Archivo {filename}\n")
    print(f"Archivo creado: {filename}")
