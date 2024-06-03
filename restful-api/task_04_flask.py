#!/usr/bin/python3
"""A module to handle simple flask requests"""
from flask import Flask, jsonify, request
import json


app = Flask(__name__)

users = { "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route('/')
def home():
    return("Welcome to the Flask API!")

@app.route('/data')
def data():
    return jsonify(users)

@app.route('/status')
def status():
    return('OK')

@app.route('/users/<username>')
def user(username):
    return (users[username])

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        data = request.get_json()
        username = data["username"]
        del data["username"]
        users[username] = data
        return ("User added")
    else:
        return('failed')

if __name__ == "__main__": app.run()
