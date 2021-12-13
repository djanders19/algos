import math
import random


def evaluate(function_type, location):
    # Make sure the input location is a list:
    if not isinstance(location, list):
        print(f"Location argument must be a list, not {type(location)}")
        return

    if function := FUNCTIONS.get(function_type):
        return function(location)

    print(f"No function found for function type {function_type}")


# The following returns a list of the outputs of each function over a range
# from start to end with <steps> steps. Note that this *only* works for one-
# dimensional inputs. We are only visualizing 1D inputs, so this is no big deal.
def evaluate_range(function_type, start, end, steps):
    if start > end:
        start, end = end, start # yay python
    
    i = start
    step = (end - start) / steps
    vals_in_range = []
    while(i <= end):
        vals_in_range.append(evaluate(function_type, [i]))
        i += step
    
    return vals_in_range



def evaluate_rosenbrock(location):
    acc = 0; # accumulator

    dimensions = len(location)

    # Sum over all the dimensions:
    for i in range(0, dimensions - 1):
        # Add the i'th term of the function:
        acc += ((100 * (location[i + 1] - location[i] ** 2))**2 + 
                (location[i] - 1)**2)

    # When finished, return the accumulator:
    return acc


# The following function evaluates the n-dimensional location argument value
# when plugged into the Rastrigin function as defined here:
# https://www.sfu.ca/~ssurjano/rastr.html
def evaluate_rastrigin(location):
    acc = 0; # accumulator

    dimensions = len(location)

    # Sum over all the dimensions:
    for i in range(0, len(location)):
        # Add the i'th term of the function:
        acc += location[i]**2 - 10 * math.cos(2 * math.pi * location[i])

    # When finished, return the accumulator:
    return (acc + 10 * len(location))


# The following function evaluates the n-dimensional location argument value
# when plugged into the Ackley function as defined here:
# https://www.sfu.ca/~ssurjano/ackley.html
def evaluate_ackley(location):
    # if you inspect the above link you'll find that the function includes
    # two summations. We keep track of these in the following vars:
    left_sum = 0
    right_sum = 0

    # Ackley can be parameterized with different constants. These are the
    # recommended constants most commonly used:
    a = 20
    b = 0.2
    c = 2 * math.pi

    dimensions = len(location)

    for i in range(0, dimensions):
        left_sum += location[i]**2
        right_sum += math.cos(c * location[i])
    

    return (-a * math.exp(-b * math.sqrt(left_sum / dimensions)) - 
            math.exp(right_sum / dimensions) + a + math.exp(1))


# The following function evaluates the n-dimensional location argument value
# when plugged into the Sphere function as defined here:
# https://www.sfu.ca/~ssurjano/spheref.html
def evaluate_sphere(location):
    acc = 0

    dimensions = len(location)

    for i in range(dimensions):
        acc += location[i] ** 2
    
    return acc


# TODO: create this
def evaluate_line_list(location):
    pass


# Create a random line list (2d only)
def make_random_line_list(starting_value, samples) -> list:
    last_val = starting_value

    graph = []
    for i in range(1, samples + 1):
        data_point = {}
        data_point["x"] = i
        direction = random.randint(0, 1)
        new_val = 0
        if direction == 0:
            new_val = last_val + random.expovariate(0.5)
        else:
            new_val = last_val - random.expovariate(0.5)
        data_point["y"] = str(round(new_val, 2))
        last_val = new_val

        graph.append(data_point)

    return graph


FUNCTIONS = {
    "rosenbrock": evaluate_rosenbrock,
    "rastrigin": evaluate_rastrigin,
    "ackley": evaluate_ackley,
    "sphere": evaluate_sphere,
    "line_list": evaluate_line_list
}
