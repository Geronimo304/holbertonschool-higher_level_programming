#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.get("/data")
def data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Return API status."""
    return "OK"


@app.get("/users/<username>")
def get_user(username):
    """Return user data for a specific username."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users.get(username))


@app.post("/add_user")
def add_user():
    """Add a new user if username is provided and not duplicated."""
    new_user = request.get_json()

    if not new_user or "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400

    username = new_user["username"]
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=True)
