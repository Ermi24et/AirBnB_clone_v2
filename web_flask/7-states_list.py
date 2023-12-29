#!/usr/bin/pyhton3
""" a script that starts a Flask web application """
from models import storage
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """ display a HTML page """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """ tear down the app context """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
