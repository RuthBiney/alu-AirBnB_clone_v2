#!/usr/bin/python3
""" Web application listening on the 0.0.0.0, port 5000 """
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ Displaying the Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Displaying  HBNB! """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.url_map.strict_slashes = False
