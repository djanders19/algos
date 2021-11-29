import functions as f
import HillClimbingAgent as hc
import RandomRestartAgent as rr
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

print("\n\nNOW TESTING HILL-CLIMBING")
print("ROSENBROCK:")
state = [rand.uniform(-5, 10) for _ in range(a.dim)]
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


print("\n\nNOW TESTING RANDOM-RESTART HILL-CLIMBING")
print("ROSENBROCK:")
state = [rand.uniform(-5, 10) for _ in range(a.dim)]
agent = rr.RandomRestartAgent(b, state, 0.01, 10, 5.0)
agent.print_state()
agent.run()
print("\nBEST ROSENBROCK SOLUTION FOUND:")
agent.print_state()

print("\n\nRASTRIGIN:")
state = [rand.uniform(-5.12, 5.12) for _ in range(b.dim)]
agent = rr.RandomRestartAgent(b, state, 0.01, 10, 5.0)
agent.print_state()
agent.run()
print("\nBEST RASTRIGIN SOLUTION FOUND:")
agent.print_state()

print("\n\nACKLEY:")
state = [rand.uniform(-32.768, 32.768) for _ in range(c.dim)]
agent = rr.RandomRestartAgent(b, state, 0.01, 10, 5.0)
agent.print_state()
agent.run()
print("\nBEST ACKLEY SOLUTION FOUND:")
agent.print_state()

print("\n\nSPHERE:")
state = [rand.uniform(-5.12, 5.12) for _ in range(d.dim)]
agent = rr.RandomRestartAgent(b, state, 0.01, 10, 5.0)
agent.print_state()
agent.run()
print("\nBEST SPHERE SOLUTION FOUND:")
agent.print_state()