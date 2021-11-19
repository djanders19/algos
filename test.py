import functions as f

rosenbrock_minimum = [1,1]
rastrigin_ackley_minimum = [0,0]

a = f.Function(len(rosenbrock_minimum), "rosenbrock")
b = f.Function(len(rosenbrock_minimum), "rastrigin")
c = f.Function(len(rosenbrock_minimum), "ackley")

num = a.eval(rosenbrock_minimum)
print(num)

num1 = b.eval(rosenbrock_minimum)
print(num1)

num2 = c.eval(rosenbrock_minimum)
print(num2)


a = f.Function(len(rastrigin_ackley_minimum), "rosenbrock")
b = f.Function(len(rastrigin_ackley_minimum), "rastrigin")
c = f.Function(len(rastrigin_ackley_minimum), "ackley")

num = a.eval(rastrigin_ackley_minimum)
print(num)

num1 = b.eval(rastrigin_ackley_minimum)
print(num1)

num2 = c.eval(rastrigin_ackley_minimum)
print(num2)