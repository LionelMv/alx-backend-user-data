#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> str:
    """return a JSON payload of the form"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users() -> str:
    """
        Implements the /users POST route.
        The end-point should expect two form data fields:
        "email" and "password".
    """
    email = request.form.get('email')
    password = request.form.get('password')

    # register user if user does not exist.
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
