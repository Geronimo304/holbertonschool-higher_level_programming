#!/usr/bin/python3
"""
task_02_requests.py
Module to fetch and process posts from JSONPlaceholder API.
"""

import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints the status code and titles."""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder and saves them into a CSV file."""
    response = requests.get(API_URL)
    
    if response.status_code == 200:
        posts = response.json()
        # Crear lista de diccionarios con id, title y body
        structured_posts = [
            {"id": post['id'], "title": post['title'], "body": post['body']}
            for post in posts
        ]
        # Escribir en CSV
        with open("posts.csv", "w", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in structured_posts:
                writer.writerow(post)
