#!/usr/bin/env python3
from os import environ
import random

from flask import Flask, jsonify, render_template


FLASK_HOST = environ.get("FLASK_HOST", "0.0.0.0")
FLASK_PORT = environ.get("PORT", 5000)
FLASK_DEBUG = environ.get("FLASK_DEBUG", False)

# NUM_DAYS = 1000
START_VAL = 98.6

SAMPLES = 1000


def make_random_graph() -> list:
    last_val = START_VAL

    graph = []
    for i in range(1, SAMPLES + 1):
        data_point = {}
        data_point["x"] = i
        direction = random.randint(0, 1)
        new_val = 0
        if direction == 0:
            new_val = last_val + random.expovariate(0.5)
        else:
            new_val = last_val - random.expovariate(0.5)
        data_point["y"] = str(round(new_val, 2))
        last_val = new_val

        graph.append(data_point)

    return graph


def make_random_points() -> list:
    num_points = random.randint(42, 69)
    return random.choices(GRAPH, k=num_points)


GRAPH = make_random_graph()
POINTS = make_random_points()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/graph")
def random_graph():
    return jsonify(GRAPH)


@app.route("/points")
def random_points():
    return jsonify(POINTS)


@app.route("/reset")
def reset_graph_and_points():
    global GRAPH
    global POINTS
    GRAPH = make_random_graph()
    POINTS = make_random_points()
    return "Created new graph and points"


if __name__ == "__main__":
    app.run(FLASK_HOST, FLASK_PORT, debug=FLASK_DEBUG)
