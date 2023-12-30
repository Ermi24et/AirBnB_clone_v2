#!/usr/bin/python3
""" a script that starts a Flask web application """

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states_list(id='0'):
    """ display a HTML page """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def remove_session(exception):
    """ tear down the app context """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
