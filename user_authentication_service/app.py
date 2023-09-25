#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    # create a dictionary with the message
    message = {"message": "Bienvenue"}

    # return the message as JSON
    return jsonify(message)


@app.route("/users", methods=["POST"])
def users():
    try:
        # get email and password from form data
        email = request.form.get("email")
        password = request.form.get("password")

        # attempt to register the user using Auth
        AUTH.register_user(email, password)

        # if successful, return a success message
        return jsonify({"email": email, "message": "user created"}), 200

    except ValueError as e:
        # handle the case where the email is already registered
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
