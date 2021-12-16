import random as rand

import agent.functions as f
from agent.hill_climbing_agent import HillClimbingAgent
from agent.random_restart_agent import RandomRestartAgent
from agent.simulated_annealing_agent import SimulatedAnnealingAgent

import csv
import sys

DIMENSIONS = int(sys.argv[2])
ITERATIONS = int(sys.argv[3])
HEADERS =   ['ros_hc', 'ros_rrhc', 'ros_sa',
             'ras_hc', 'ras_rrhc', 'ras_sa',
             'ack_hc', 'ack_rrhc', 'ack_sa',
             'sphere_hc', 'sphere_rrhc', 'sphere_sa']

SCHEDULE = [x / 100000.0 for x in range(2500000, 0, -1)]

result_row = []

f = open(sys.argv[1], 'w')
writer = csv.writer(f)
writer.writerow(HEADERS)

for i in range(ITERATIONS):
    print(i)
    # ROSENBROCK:
    state = [rand.uniform(-2.048, 2.048) for _ in range(DIMENSIONS)]
    agent = HillClimbingAgent("rosenbrock", state, 0.01)
    agent.run()
    result_row.append(agent.value)

    agent = RandomRestartAgent("rosenbrock", state, 0.01, 10, 2.048)
    agent.run()
    result_row.append(agent.value)

    print(f"Rosenbrock iteration {i}")
    agent = SimulatedAnnealingAgent("rosenbrock", state, 0.01, SCHEDULE)
    agent.run()
    result_row.append(agent.value)


    # RASTRIGIN:
    state = [rand.uniform(-5.12, 5.12) for _ in range(DIMENSIONS)]
    agent = HillClimbingAgent("rastrigin", state, 0.01)
    agent.run()
    result_row.append(agent.value)

    agent = RandomRestartAgent("rastrigin", state, 0.01, 10, 5.12)
    agent.run()
    result_row.append(agent.value)

    print(f"Rastrigin iteration {i}")
    agent = SimulatedAnnealingAgent("rastrigin", state, 0.01, SCHEDULE)
    agent.run()
    result_row.append(agent.value)


    # ACKLEY:
    state = [rand.uniform(-32.768, 32.768) for _ in range(DIMENSIONS)]
    agent = HillClimbingAgent("ackley", state, 0.01)
    agent.run()
    result_row.append(agent.value)

    agent = RandomRestartAgent("ackley", state, 0.01, 10, 32.768)
    agent.run()
    result_row.append(agent.value)

    print(f"Ackley iteration {i}")
    agent = SimulatedAnnealingAgent("ackley", state, 0.01, SCHEDULE)
    agent.run()
    result_row.append(agent.value)


    # SPHERE:
    state = [rand.uniform(-5.12, 5.12) for _ in range(DIMENSIONS)]
    agent = HillClimbingAgent("sphere", state, 0.01)
    agent.run()
    result_row.append(agent.value)

    agent = RandomRestartAgent("sphere", state, 0.01, 10, 5.12)
    agent.run()
    result_row.append(agent.value)

    print(f"Sphere iteration {i}")
    agent = SimulatedAnnealingAgent("sphere", state, 0.01, SCHEDULE)
    agent.run()
    result_row.append(agent.value)

    writer.writerow(result_row)
    result_row = []



f.close()