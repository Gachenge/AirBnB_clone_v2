#!/usr/bin/python3
"""
flask web app listening on 0.0.0.0:5000
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """remove current session after each request"""
    storage.close()


@app.route("/states", strict_slashes=False)
def stat():
    """list all states in dbstorage"""
    states = storage.all("State")
    return render_template("9-states.html", states=states, id='no')


@app.route("/states/<id>", strict_slashes=False)
def state(id):
    """identify state by id"""
    for states in storage.all("State").values():
        if states.id == id:
            return render_template("9-states.html", states=states, id='yes')
    return render_template("9-states.html")
        

if __name__ =="__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
