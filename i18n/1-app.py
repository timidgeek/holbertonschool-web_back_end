#!/usr/bin/env python3
""" basic babel setup task one """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ babel config module """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """renders `index.html` doc"""
    return render_template('0-index.html')


if __name__ == 'main':
    app.run()
