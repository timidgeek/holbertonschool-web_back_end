#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    # create a dictionary with the message
    message = {"message": "Bienvenue"}

    # return the message as JSON
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
