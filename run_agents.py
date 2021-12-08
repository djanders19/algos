import random as rand

import agent.functions as f
import agent.HillClimbingAgent as hc
import agent.RandomRestartAgent as rr
import agent.SimulatedAnnealingAgent as sa


ROSENBROCK_MINIMUM = [1,1]
RASTRIGIN_ACKLEY_SPHERE_MINIMUM = [0,0]


num = f.evaluate("rosenbrock", ROSENBROCK_MINIMUM)
print(num)

num1 = f.evaluate("rastrigin", ROSENBROCK_MINIMUM)
print(num1)

num2 = f.evaluate("ackley", ROSENBROCK_MINIMUM)
print(num2)

num3 = f.evaluate("sphere", ROSENBROCK_MINIMUM)
print(num3)


num = f.evaluate("rosenbrock", RASTRIGIN_ACKLEY_SPHERE_MINIMUM)
print(num)

num1 = f.evaluate("rastrigin", RASTRIGIN_ACKLEY_SPHERE_MINIMUM)
print(num1)

num2 = f.evaluate("ackley", RASTRIGIN_ACKLEY_SPHERE_MINIMUM)
print(num2)

num3 = f.evaluate("sphere", RASTRIGIN_ACKLEY_SPHERE_MINIMUM)
print(num3)


# Hill-Climbing Tests:
print("\n\nNOW TESTING HILL-CLIMBING")
print("ROSENBROCK:")
state = [rand.uniform(-2.048, 2.048) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = hc.HillClimbingAgent("rosenbrock", state, 0.01)
agent.print_state()
agent.run()
print("\nBEST ROSENBROCK SOLUTION FOUND:")
agent.print_state()

print("\n\nRASTRIGIN:")
state = [rand.uniform(-5.12, 5.12) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = hc.HillClimbingAgent("rastrigin", state, 0.01)
agent.print_state()
agent.run()
print("\nBEST RASTRIGIN SOLUTION FOUND:")
agent.print_state()

print("\n\nACKLEY:")
state = [rand.uniform(-32.768, 32.768) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = hc.HillClimbingAgent("ackley", state, 0.01)
agent.print_state()
agent.run()
print("\nBEST ACKLEY SOLUTION FOUND:")
agent.print_state()

print("\n\nSPHERE:")
state = [rand.uniform(-5.12, 5.12) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = hc.HillClimbingAgent("sphere", state, 0.01)
agent.print_state()
agent.run()
print("\nBEST SPHERE SOLUTION FOUND:")
agent.print_state()


# RR-Hill Climbing Tests:
print("\n\nNOW TESTING RANDOM-RESTART HILL-CLIMBING")
print("ROSENBROCK:")
state = [rand.uniform(-2.048, 2.048) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = rr.RandomRestartAgent("rosenbrock", state, 0.01, 10, 2.048)
agent.print_state()
agent.run()
print("\nBEST ROSENBROCK SOLUTION FOUND:")
agent.print_state()

print("\n\nRASTRIGIN:")
state = [rand.uniform(-5.12, 5.12) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = rr.RandomRestartAgent("rastrigin", state, 0.01, 10, 5.12)
agent.print_state()
agent.run()
print("\nBEST RASTRIGIN SOLUTION FOUND:")
agent.print_state()

print("\n\nACKLEY:")
state = [rand.uniform(-32.768, 32.768) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = rr.RandomRestartAgent("ackley", state, 0.01, 10, 32.768)
agent.print_state()
agent.run()
print("\nBEST ACKLEY SOLUTION FOUND:")
agent.print_state()

print("\n\nSPHERE:")
state = [rand.uniform(-5.12, 5.12) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = rr.RandomRestartAgent("sphere", state, 0.01, 10, 5.12)
agent.print_state()
agent.run()
print("\nBEST SPHERE SOLUTION FOUND:")
agent.print_state()


# Simulated annealing tests:
print("\n\nNOW TESTING SIMULATED ANNEALING")
schedule = [x / 1000.0 for x in range(25000, 0, -1)]

print("ROSENBROCK:")
state = [rand.uniform(-2.048, 2.048) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = sa.SimulatedAnnealingAgent("rosenbrock", state, 0.1, schedule)
agent.print_state()
agent.run()
print("\nBEST ROSENBROCK SOLUTION FOUND:")
agent.print_state()

print("\n\nRASTRIGIN:")
state = [rand.uniform(-5.12, 5.12) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = sa.SimulatedAnnealingAgent("rastrigin", state, 0.1, schedule)
agent.print_state()
agent.run()
print("\nBEST RASTRIGIN SOLUTION FOUND:")
agent.print_state()

print("\n\nACKLEY:")
state = [rand.uniform(-32.768, 32.768) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = sa.SimulatedAnnealingAgent("ackley", state, 0.1, schedule)
agent.print_state()
agent.run()
print("\nBEST ACKLEY SOLUTION FOUND:")
agent.print_state()

print("\n\nSPHERE:")
state = [rand.uniform(-5.12, 5.12) for _ in range(len(RASTRIGIN_ACKLEY_SPHERE_MINIMUM))]
agent = sa.SimulatedAnnealingAgent("sphere", state, 0.1, schedule)
agent.print_state()
agent.run()
print("\nBEST SPHERE SOLUTION FOUND:")
agent.print_state()
