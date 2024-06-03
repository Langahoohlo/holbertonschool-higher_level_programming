#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

# In-memory storage for users
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password2"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """Verify user credentials for basic authentication.

    Args:
        username (str): Username.
        password (str): Password.

    Returns:
        bool: True if credentials are valid, False otherwise.
    """
    if username in users and check_password_hash(users[username]['password'], password):
        return username

@app.route('/')
def home():
    """Home route.

    Returns:
        str: Welcome message.
    """
    return "Welcome to the Flask API!"

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Protected route with basic authentication.

    Returns:
        str: Access granted message.
    """
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """Login route for JWT authentication.

    Returns:
        dict: JWT token if credentials are valid.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity={'username': username, 'role': users[username]['role']})
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Protected route with JWT authentication.

    Returns:
        str: Access granted message.
    """
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Protected route for admin role with JWT authentication.

    Returns:
        str: Admin access message.
    """
    current_user = get_jwt_identity()
    if current_user['role'] == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token error.

    Args:
        err (str): Error message.

    Returns:
        dict: Error message with status code.
    """
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token error.

    Args:
        err (str): Error message.

    Returns:
        dict: Error message with status code.
    """
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token error.

    Args:
        err (str): Error message.

    Returns:
        dict: Error message with status code.
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401
