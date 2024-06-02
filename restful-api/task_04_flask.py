#!/usr/bin/python3
"""Making a basic api to send anfd get data"""
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return jsonify({"status": "OK"})

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in users:
        return jsonify({"error": "Duplicate username"}), 400
    
    users[username] = {
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]})

@app.before_request
def before_request_func():
    print("This runs before each request.")

@app.after_request
def after_request_func(response):
    print("This runs after each request.")
    return response

@app.teardown_request
def teardown_request_func(error=None):
    print("This runs after the request is finished, whether there was an error or not.")

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "This page does not exist"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "An internal error occurred"}), 500

if __name__ == "__main__":
    app.run(debug=True)

