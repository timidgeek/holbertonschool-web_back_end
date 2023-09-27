#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


auth = None
auth_type = os.getenv('AUTH_TYPE', 'basic')

if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()

if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

if auth_type == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def forbidden(error) -> str:
    """
    forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403

# Create an error handler for 401 Unauthorized


@app.errorhandler(401)
def unauthorized(error) -> str:
    """
    unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.route('/api/v1/unauthorized', strict_slashes=False)
def unauthorized_route():
    """
    unauthorized route - abort
    """
    abort(401)


@app.before_request
def before_request():
    """
    runs before every request
    """
    # ensure `current_user` is available for all requests
    request.current_user = auth.current_user(request)

    path_list = ['/api/v1/status/',
                 '/api/v1/unauthorized',
                 '/api/v1/forbidden',
                 '/api/v1/auth_session/login/']
    if auth and auth.require_auth(request.path, path_list):
        if auth.authorization_header(request) is None \
            and auth.session_cookie(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
