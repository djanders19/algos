import math


def evaluate(function_type, location):
    # Make sure the input location is a list:
    if not isinstance(location, list):
        print(f"Location argument must be a list, not {type(location)}")
        return

    if function := FUNCTIONS.get(function_type):
        return function(location)

    print(f"No function found for function type {function_type}")


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


FUNCTIONS = {
    "rosenbrock": evaluate_rosenbrock,
    "rastrigin": evaluate_rastrigin,
    "ackley": evaluate_ackley,
    "sphere": evaluate_sphere
}