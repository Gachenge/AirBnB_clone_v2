#!/usr/bin/python3
"""
script that starts a flask web app
host = 0.0.0.0 on port 5000
no debug
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display a greeting message"""
    return ('Hello HBNB!')


@app.route("/hbnb", strict_slashes=False)
def rude():
    """no greeting"""
    return ('HBNB')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
