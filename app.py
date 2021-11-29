#!/usr/bin/env python3
from datetime import datetime, timedelta
import random

from flask import Flask, jsonify, render_template


NUM_DAYS = 1000
START_VAL = 98.6

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/graph")
def random_graph():
    base = datetime.today()
    date_list = [base - timedelta(days=x) for x in range(NUM_DAYS)]

    last_val = START_VAL

    chart = []
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

        chart.append(data_point)

    return jsonify(chart)


if __name__ == "__main__":
	app.run("0.0.0.0", 5000, debug=True)
