#!/usr/bin/python3
"""web app listening on host: 0.0.0.0 port: 5000
use storage: filestorage or dbstorage
"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """close session after each request"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def display():
    """display a web page"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
