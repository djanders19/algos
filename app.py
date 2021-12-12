#!/usr/bin/env python3
from datetime import datetime, timedelta
import random

from flask import Flask, jsonify, render_template


NUM_DAYS = 1000
START_VAL = 98.6


def make_random_graph() -> list:
    base = datetime.today()
    date_list = [base - timedelta(days=x) for x in range(NUM_DAYS)]

    last_val = START_VAL

    graph = []
    for date in date_list:
        data_point = {}
        data_point["date"] = date.strftime("%Y-%m-%d")
        direction = random.randint(0, 1)
        new_val = 0
        if direction == 0:
            new_val = last_val + random.expovariate(0.5)
        else:
            new_val = last_val - random.expovariate(0.5)
        data_point["value"] = str(round(new_val, 2))
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


if __name__ == "__main__":
	app.run("0.0.0.0", 5000, debug=True)
