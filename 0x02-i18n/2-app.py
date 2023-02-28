#!/usr/bin/env python3
"""
Then instantiate the Babel object in your app.
Store it in a module-level variable named babel.

In order to configure available languages in our
app you will create a Config class that has
LANGUAGES class attribute equal to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and
timezone ("UTC").

Use that class as config for your Flask app.
"""


from flask import Flask, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configuration class for appilication
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello():
    """
    A route that renders index.html templat
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """Create a get_locale function with the babel.localeselector decorator.
    Use request.accept_languages to determine the
    best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])
