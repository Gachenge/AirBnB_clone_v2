#!/usr/bin/python3
"""
script that starts a flask web app
host = 0.0.0.0 on port 5000
no debug
"""
from flask import Flask
from flask import render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def temnum(n):
    return render_template("5-number.html", numb=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def eveodd(n):
    if n % 2 == 0:
        even = '{} is even'.format(n)
    else:
        even = '{} is odd'.format(n)
    return render_template("6-number_odd_or_even.html", evod=even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
