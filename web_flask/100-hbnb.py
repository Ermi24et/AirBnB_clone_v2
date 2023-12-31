#!/usr/bin/python3
""" a script that starts a Flask web application """

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def states_list(id='0'):
    """ display a HTML page """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    place = storage.all(Place).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities, place=place, id=id)


@app.teardown_appcontext
def remove_session(exception):
    """ tear down the app context """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
