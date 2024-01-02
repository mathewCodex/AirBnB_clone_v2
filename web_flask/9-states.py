#!/usr/bin/python3
"""Starts a Flask app"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """displays an html page with a list of all states"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """displays an html page with info about <id>"""
    for state in storgae.all("States").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states..html")


@app.teardown_appcontenxt
def teardown(exc):
    """Remove the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
