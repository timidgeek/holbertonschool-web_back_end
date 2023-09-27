#!/usr/bin/env python3
"""
new Flask view that handles all routes
for the Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route("/auth_session/login", METHOD=["POST"], strict_slashes=False)
def login():
    """
    route for POST /api/v1/auth_session/login
    """
    # get email, handle missing errors
    email = request.form.get('email')
    if not email:
        return jsonify({'error': 'email missing'}), 400
    try:
        user = User.search({'email': email})
    except Exception:
        return jsonify({'error': 'no user found for this email'}), 404
    if not user:
        return jsonify({'error': 'no user found for this email'}), 404
    user = user[0]

    # get password, handle missing errors
    password = request.form.get('password')
    if not password:
        return jsonify({'error': 'password missing'}), 400
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # create session_id for the user_id
    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    SESSION_NAME = getenv('SESSION_NAME')

    # set the cookie to the response
    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, session_id)
    return response
