#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")

def route():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status", methods=["GET"])
def status():
    return "OK", 200

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__": app.run()