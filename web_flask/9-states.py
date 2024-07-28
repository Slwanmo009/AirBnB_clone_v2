#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Displays a HTML page with the list of all State objects
    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """
    Displays a HTML page with the list of City objects linked to the State
    """
    states = storage.all(State)
    state = states.get(f'State.{id}')
    return render_template('9-state.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
