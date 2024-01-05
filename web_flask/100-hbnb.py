#!/usr/bin/python3
"""Starts a web app"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity



app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb_filters():
    """display the main Hbnb filters page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    cities = storage.all(City)
    return render_template("100-hbnb.html",
                            states=states, amenities=amenities, places=places, cities=cities)




@app.teardown_appcontext
def teardown(exc):
    """remove session"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
