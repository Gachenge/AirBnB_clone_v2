#!/usr/bin/python3
from flask import Flask
from flask import render_template

"""
script that starts a flask web app
"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display a greeting message"""

    return ('Hello HBNB!')


@app.route("/hbnb", strict_slashes=False)
def rude():
    """no greeting"""

    return ('HBNB')


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """display some text"""
    return ("C {}".format(text).replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def ptext(text="is cool"):
    """display how cool python is"""
    return ("Python {}".format(text).replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """check if n is a number"""
    return ("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
