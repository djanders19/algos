#!/usr/bin/env python3
from os import environ
import random

from flask import Flask, jsonify, render_template

import agent.functions
from agent.hill_climbing_agent import HillClimbingAgent
from agent.random_restart_agent import RandomRestartAgent
from agent.simulated_annealing_agent import SimulatedAnnealingAgent


FLASK_HOST = environ.get("FLASK_HOST", "0.0.0.0")
FLASK_PORT = environ.get("PORT", 5000)
FLASK_DEBUG = environ.get("FLASK_DEBUG", True)

START_VAL = 98.6

SAMPLES = 1000

RASTRIGIN_ACKLEY_SPHERE_MINIMUM = [0,0]

agent.functions.make_global_line_list(START_VAL, SAMPLES)
GRAPH = agent.functions.line_list

print(f"GRAPH: {GRAPH}")


RANGES = {
    "ackley": [-32, 32],
    "rastrigin": [-5, 5],
    "sphere": [-5, 5],
    "line_list": [0, 1000]
}

AGENTS = {
    "random_restart": RandomRestartAgent,
    "simulated_annealing": SimulatedAnnealingAgent
}


def make_random_points(graph=GRAPH) -> list:
    num_points = random.randint(42, 84)
    return random.choices(graph, k=num_points)


POINTS = make_random_points()


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ackley")
def render_ackley_page():
    return render_template("ackley.html")


@app.route("/rastrigin")
def render_rastrigin_page():
    return render_template("rastrigin.html")


@app.route("/sphere")
def render_sphere_page():
    return render_template("sphere.html")


@app.route("/hill_climbing/ackley")
def render_hc_ackley_page():
    return render_template("ackley_hc.html")


@app.route("/hill_climbing/line_list")
def render_hc_line_list_page():
    return render_template("line_list_hc.html")


@app.route("/hill_climbing/rastrigin")
def render_hc_rastrigin_page():
    return render_template("rastrigin_hc.html")


@app.route("/hill_climbing/sphere")
def render_hc_sphere_page():
    return render_template("sphere_hc.html")


@app.route("/random_restart/ackley")
def render_rr_ackley_page():
    return render_template("ackley_rr.html")


@app.route("/random_restart/line_list")
def render_rr_line_list_page():
    return render_template("line_list_rr.html")


@app.route("/random_restart/rastrigin")
def render_rr_rastrigin_page():
    return render_template("rastrigin_rr.html")


@app.route("/random_restart/sphere")
def render_rr_sphere_page():
    return render_template("sphere_rr.html")


@app.route("/simulated_annealing/ackley")
def render_sa_ackley_page():
    return render_template("ackley_sa.html")


@app.route("/simulated_annealing/line_list")
def render_sa_line_list_page():
    return render_template("line_list_sa.html")


@app.route("/simulated_annealing/rastrigin")
def render_sa_rastrigin_page():
    return render_template("rastrigin_sa.html")


@app.route("/simulated_annealing/sphere")
def render_sa_sphere_page():
    return render_template("sphere_sa.html")


@app.route("/graph")
def random_graph():
    return jsonify(GRAPH)


def get_x_value(samples, function_min, function_max, input_value):
    function_range = function_max - function_min
    return (((input_value - 1) * function_range) / samples) + function_min


@app.route("/graph/<function_type>")
def function_graph(function_type):
    sf = RANGES.get(function_type)

    function_max = sf[1]
    function_min = sf[0]

    y_values = agent.functions.evaluate_range(function_type, function_min, function_max, SAMPLES)
    graph = [{"x": get_x_value(SAMPLES, function_min, function_max, index), "y": value} for index, value in enumerate(y_values)]

    return jsonify(graph)


@app.route("/points")
def random_points():
    return jsonify(POINTS)


@app.route("/points/<function_type>")
def function_points(function_type):
    sf = RANGES.get(function_type)
    function_max = sf[1]
    function_min = sf[0]
    y_values = agent.functions.evaluate_range(function_type, sf[0], sf[1], SAMPLES)
    graph = [{"x": get_x_value(SAMPLES, function_min, function_max, index), "y": value} for index, value in enumerate(y_values)]

    return jsonify(make_random_points(graph))


@app.route("/points/<agent_type>/<function_type>")
def agent_function_points(agent_type, function_type):
    global GRAPH
    sf = RANGES.get(function_type)
    if function_type == "line_list":
        state = GRAPH
    else:
        state = [random.uniform(sf[0], sf[1])]
    agent = None
    if agent_type == "random_restart":
        agent = RandomRestartAgent(function_type, state, 0.01, 10, sf[1])
    elif agent_type == "hill_climbing":
        agent = HillClimbingAgent(function_type, state, 0.01)
    elif agent_type == "simulated_annealing":
        schedule = [x / 1000.0 for x in range(25000, 0, -1)]
        agent = SimulatedAnnealingAgent(function_type, state, 0.1, schedule)
    agent.run()
    points = []
    if agent_type in ["random_restart"]:
        paths = agent.path
        path = [item for sublist in paths for item in sublist]
    elif agent_type in ["hill_climbing","simulated_annealing"]:
        path = agent.path
        if agent_type == "simulated_annealing":
            path = agent.path[::1000]
    points = [{"x": point[0][0], "y": point[1]} for point in path] 

    return jsonify(points)


@app.route("/reset")
def reset_graph_and_points():
    global GRAPH
    global POINTS
    GRAPH = agent.functions.make_random_line_list(START_VAL, SAMPLES)
    POINTS = make_random_points()
    return "Created new graph and points"


if __name__ == "__main__":
    app.run(FLASK_HOST, FLASK_PORT, debug=FLASK_DEBUG)
