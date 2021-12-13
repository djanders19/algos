#!/usr/bin/env python3
from os import environ
import random

from flask import Flask, jsonify, render_template

from agent.functions import evaluate, make_random_line_list


FLASK_HOST = environ.get("FLASK_HOST", "0.0.0.0")
FLASK_PORT = environ.get("PORT", 5000)
FLASK_DEBUG = environ.get("FLASK_DEBUG", False)

START_VAL = 98.6

SAMPLES = 1000


def make_random_points() -> list:
    num_points = random.randint(42, 69)
    return random.choices(GRAPH, k=num_points)


GRAPH = make_random_line_list(START_VAL, SAMPLES)
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
    GRAPH = make_random_line_list(START_VAL, SAMPLES)
    POINTS = make_random_points()
    return "Created new graph and points"


if __name__ == "__main__":
    app.run(FLASK_HOST, FLASK_PORT, debug=FLASK_DEBUG)
