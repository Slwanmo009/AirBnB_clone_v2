#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays a HTML page with a list of all State objects present in DBStorage,
    sorted by name (A->Z).
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown(exception):
    """
    Remove the current SQLAlchemy session.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
