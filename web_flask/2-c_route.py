#!/usr/bin/python3
"""This module starts a flask app on 0.0.0.0:5000"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def main():
    """Returns a text"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/c/<txt>', strict_slashes=False)
def text(txt):
    """Returns a text passed as param"""
    return 'c {}'.format(txt.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
