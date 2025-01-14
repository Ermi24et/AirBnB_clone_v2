#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ returns HBNB """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """ display C followed by the value of the text variable """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def is_cool(text='is cool'):
    """ display Python followed by the value of the text variable """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def is_number(n):
    """ display n is a number if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def num_teplate(n):
    """ display HTML page if n is an integer """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
