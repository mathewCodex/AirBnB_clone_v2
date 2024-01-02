#!/usr/bin/python3
""" starts aFlask web app
listening on port 5000
Routes:
    /: displays 'Hello HBNB'
    /hbnb displays 'HBNB'
"""
from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb" strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display "C ", followed by the val of the textvar"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display "python ", followed by the val"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def iamnumber(n):
    """display "n is a number" if its an int"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
