#!/usr/bin/python3
"""A module to handle simple flask requests"""
from flask import Flask, jsonify, request
import json


app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return("Welcome to the Flask API!")

@app.route('/data')
def data():
    if users:
        return jsonify(users.keys())
    return 'No users'

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def user(username):
    if username in users.keys():
        return (users[username])
    return '{"error": "User not found"}', 400


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        data = request.get_json()
        response_data = data
        username = data["username"]
        if not username:
            return 'username is empty', 400
        if username in users.keys():
            return 'username already exists', 400
        del data["username"]
        users[username] = data
        response = {}
        response["message"] = "User added"
        response["user"] = response_data
        return jsonify(response), 201
    else:
        return 'failed', 400

if __name__ == "__main__": app.run()
