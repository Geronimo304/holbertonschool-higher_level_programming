#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """Obtiene y muestra los títulos de las publicaciones desde JSONPlaceholder"""
    url = "https://jsonplaceholder.typicode.com/posts"
    reply = requests.get(url)

    print(f"Status Code: {reply.status_code}")

    if reply.ok:
        all_posts = reply.json()
        for i, entry in enumerate(all_posts, start=1):
            print(f"{i}. {entry.get('title')}")

def fetch_and_save_posts():
    """Guarda las publicaciones en un archivo CSV con id, título y contenido"""
    endpoint = "https://jsonplaceholder.typicode.com/posts"
    resultado = requests.get(endpoint)

    if resultado.status_code == 200:
        publicaciones = resultado.json()
        datos_csv = []

        for p in publicaciones:
            datos_csv.append({
                "id": p.get("id"),
                "titulo": p.get("title"),
                "contenido": p.get("body")
            })

        with open("posts.csv", mode="w", encoding="utf-8", newline="") as archivo_csv:
            columnas = ["id", "titulo", "contenido"]
            escritor = csv.DictWriter(archivo_csv, fieldnames=columnas)
            escritor.writeheader()
            for fila in datos_csv:
                escritor.writerow(fila)
