#!/usr/bin/python3
""" a script that starts a Flask web application """

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def states_list():
    """ display a HTML page """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def remove_session(exception):
    """ tear down the app context """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
