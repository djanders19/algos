import functions as f
import HillClimbingAgent as hc

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

print("\n\n NOW TESTING HILL-CLIMBING")
agent = hc.HillClimbingAgent(d, rosenbrock_minimum, 0.01)
agent.print_state()
agent.run_for_n_iterations(1)
agent.run_for_n_iterations(5)
agent.run_for_n_iterations(1000)
#agent.run()