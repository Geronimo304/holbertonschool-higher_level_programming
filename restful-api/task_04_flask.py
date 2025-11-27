from flask import Flask, jsonify, request


app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return f"Welcome to the Flask API!"


@app.get("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return f"OK"


@app.get("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users.get(username))


@app.post("/add_user")
def add_user():
    new_user = request.get_json()

    if not new_user or "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400

    users[new_user["username"]] = new_user

    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run(debug=True)
