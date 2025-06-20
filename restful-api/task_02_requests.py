#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """Hace una solicitud GET a la API y muestra los títulos de los posts."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Obtiene los posts de la API y los guarda en un archivo CSV con los encabezados esperados."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data = []
        for post in posts:
            data.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)

