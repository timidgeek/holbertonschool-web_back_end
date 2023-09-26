#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route("/sessions", methods=["POST"])
def login():
    """
    returns a JSON payload of the form
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email=email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response

    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout():
    """
    finds user with `session_id`, destroys session,
    redirects user to `GET /`,
    if user DNE, respond `403`
    """
    # get session_id
    session_id = request.cookies.get("session_id")

    if session_id:
        # get user
        user = AUTH.get_user_from_session_id(session_id=session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect("/")

    abort(403)  # user does not exist


@app.route("/profile", method=["GET"])
def profile():
    """
    get profile
    """
    # get session_id
    session_id = request.cookies.get("session_id")

    if session_id:
        # get user
        user = AUTH.get_user_from_session_id(session_id=session_id)
        if user:
            return jsonify({"email": user.email}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
