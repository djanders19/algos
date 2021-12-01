import functions as f
import HillClimbingAgent as hc
import RandomRestartAgent as rr
import SimulatedAnnealingAgent as sa
import random as rand
rosenbrock_minimum = [1,1]
rastrigin_ackley_sphere_minimum = [0,0]

a = f.Function(len(rosenbrock_minimum), "rosenbrock")
b = f.Function(len(rosenbrock_minimum), "rastrigin")
c = f.Function(len(rosenbrock_minimum), "ackley")
d = f.Function(len(rosenbrock_minimum), "sphere")

num = a.eval(rosenbrock_minimum)
print(num)

num1 = b.eval(rosenbrock_minimum)
print(num1)

num2 = c.eval(rosenbrock_minimum)
print(num2)

num3 = d.eval(rosenbrock_minimum)
print(num3)


a = f.Function(len(rastrigin_ackley_sphere_minimum), "rosenbrock")
b = f.Function(len(rastrigin_ackley_sphere_minimum), "rastrigin")
c = f.Function(len(rastrigin_ackley_sphere_minimum), "ackley")
d = f.Function(len(rastrigin_ackley_sphere_minimum), "sphere")

num = a.eval(rastrigin_ackley_sphere_minimum)
print(num)

num1 = b.eval(rastrigin_ackley_sphere_minimum)
print(num1)

num2 = c.eval(rastrigin_ackley_sphere_minimum)
print(num2)

num3 = d.eval(rastrigin_ackley_sphere_minimum)
print(num3)


# Hill-Climbing Tests:
print("\n\nNOW TESTING HILL-CLIMBING")
print("ROSENBROCK:")
state = [rand.uniform(-2.048, 2.048) for _ in range(a.dim)]
agent = hc.HillClimbingAgent(a, state, 0.01)
agent.print_state()
agent.run()
print("\nBEST ROSENBROCK SOLUTION FOUND:")
agent.print_state()

print("\n\nRASTRIGIN:")
state = [rand.uniform(-5.12, 5.12) for _ in range(b.dim)]
agent = hc.HillClimbingAgent(b, state, 0.01)
agent.print_state()
agent.run()
print("\nBEST RASTRIGIN SOLUTION FOUND:")
agent.print_state()

print("\n\nACKLEY:")
state = [rand.uniform(-32.768, 32.768) for _ in range(c.dim)]
agent = hc.HillClimbingAgent(c, state, 0.01)
agent.print_state()
agent.run()
print("\nBEST ACKLEY SOLUTION FOUND:")
agent.print_state()

print("\n\nSPHERE:")
state = [rand.uniform(-5.12, 5.12) for _ in range(d.dim)]
agent = hc.HillClimbingAgent(d, state, 0.01)
agent.print_state()
agent.run()
print("\nBEST SPHERE SOLUTION FOUND:")
agent.print_state()


# RR-Hill Climbing Tests:
print("\n\nNOW TESTING RANDOM-RESTART HILL-CLIMBING")
print("ROSENBROCK:")
state = [rand.uniform(-2.048, 2.048) for _ in range(a.dim)]
agent = rr.RandomRestartAgent(a, state, 0.01, 10, 2.048)
agent.print_state()
agent.run()
print("\nBEST ROSENBROCK SOLUTION FOUND:")
agent.print_state()

print("\n\nRASTRIGIN:")
state = [rand.uniform(-5.12, 5.12) for _ in range(b.dim)]
agent = rr.RandomRestartAgent(b, state, 0.01, 10, 5.12)
agent.print_state()
agent.run()
print("\nBEST RASTRIGIN SOLUTION FOUND:")
agent.print_state()

print("\n\nACKLEY:")
state = [rand.uniform(-32.768, 32.768) for _ in range(c.dim)]
agent = rr.RandomRestartAgent(c, state, 0.01, 10, 32.768)
agent.print_state()
agent.run()
print("\nBEST ACKLEY SOLUTION FOUND:")
agent.print_state()

print("\n\nSPHERE:")
state = [rand.uniform(-5.12, 5.12) for _ in range(d.dim)]
agent = rr.RandomRestartAgent(d, state, 0.01, 10, 5.12)
agent.print_state()
agent.run()
print("\nBEST SPHERE SOLUTION FOUND:")
agent.print_state()


# Simulated annealing tests:
print("\n\nNOW TESTING SIMULATED ANNEALING")
schedule = [x / 1000.0 for x in range(25000, 0, -1)]

print("ROSENBROCK:")
state = [rand.uniform(-2.048, 2.048) for _ in range(a.dim)]
agent = sa.SimulatedAnnealingAgent(a, state, 0.1, schedule)
agent.print_state()
agent.run()
print("\nBEST ROSENBROCK SOLUTION FOUND:")
agent.print_state()

print("\n\nRASTRIGIN:")
state = [rand.uniform(-5.12, 5.12) for _ in range(b.dim)]
agent = sa.SimulatedAnnealingAgent(b, state, 0.1, schedule)
agent.print_state()
agent.run()
print("\nBEST RASTRIGIN SOLUTION FOUND:")
agent.print_state()

print("\n\nACKLEY:")
state = [rand.uniform(-32.768, 32.768) for _ in range(c.dim)]
agent = sa.SimulatedAnnealingAgent(c, state, 0.1, schedule)
agent.print_state()
agent.run()
print("\nBEST ACKLEY SOLUTION FOUND:")
agent.print_state()

print("\n\nSPHERE:")
state = [rand.uniform(-5.12, 5.12) for _ in range(d.dim)]
agent = sa.SimulatedAnnealingAgent(d, state, 0.1, schedule)
agent.print_state()
agent.run()
print("\nBEST SPHERE SOLUTION FOUND:")
agent.print_state()