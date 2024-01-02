#!/usr/bin/python3
"""A simple Falsk app that listen on
    localhost 5000
    Routes:
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """displays 'C' followed by the val of <text>
    Replaces any '_' with slashes
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """displays 'python followed by the val of text
    replaces  any '_' in text with slashes
    """
    text = text.replace("_", " ")
    return "python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """displays 'n is a number' only if <n> is an int"""
    return "{} is anumber".format(n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """displays an html page if n is an int
    and states if its an odd or even number
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
