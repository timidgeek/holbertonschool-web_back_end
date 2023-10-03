#!/usr/bin/env python3
""" basic Flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """renders `index.html` doc"""
    return render_template('0-index.html')


if __name__ == 'main':
    app.run()
