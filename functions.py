import math

class Function:
    def __init__(self, dimension, function):
        self.dim = dimension
        self.type = function

    def eval(self, location):
        # Make sure the input location is a list:
        if not isinstance(location, list):
            print("Function.eval(): didn't pass list as location argument.")
            return

        # Make sure input location is of the correct dimension:
        if (len(location) != self.dim):
            print("Function.eval(): location is not in correct dimension.")
            return;
        
        # Evaluate based on the type of the function:
        if (self.type == "rosenbrock"):
            print("Evaluating Rosenbrock function")
            return self.eval_rosenbrock(location)
        if (self.type == "rastrigin"):
            print("Evaluating Rastrigin function")
            return self.eval_rastrigin(location)
        if (self.type == "ackley"):
            print("Evaluating Ackley function")
            return self.eval_ackley(location)
        if (self.type == "sphere"):
            return self.eval_sphere(location)
        
        print("Function.eval(): unrecognized function type. Returning.")
        return


    # The following function evaluates the n-dimensional location argument value
    # when plugged into the Rosenbrock function as defined here:
    # https://www.sfu.ca/~ssurjano/rosen.html
    def eval_rosenbrock(self, location):
        acc = 0; # accumulator

        # Sum over all the dimensions:
        for i in range(0, self.dim - 1):
            # Add the i'th term of the function:
            acc += ((100 * (location[i + 1] - location[i] ** 2))**2 + 
                    (location[i] - 1)**2)

        # When finished, return the accumulator:
        return acc


    # The following function evaluates the n-dimensional location argument value
    # when plugged into the Rastrigin function as defined here:
    # https://www.sfu.ca/~ssurjano/rastr.html
    def eval_rastrigin(self, location):
        acc = 0; # accumulator

        # Sum over all the dimensions:
        for i in range(0, self.dim):
            # Add the i'th term of the function:
            acc += location[i]**2 - 10 * math.cos(2 * math.pi * location[i])

        # When finished, return the accumulator:
        return (acc + 10 * self.dim)


    # The following function evaluates the n-dimensional location argument value
    # when plugged into the Ackley function as defined here:
    # https://www.sfu.ca/~ssurjano/ackley.html
    def eval_ackley(self, location):
        # if you inspect the above link you'll find that the function includes
        # two summations. We keep track of these in the following vars:
        left_sum = 0
        right_sum = 0

        # Ackley can be parameterized with different constants. These are the
        # recommended constants most commonly used:
        a = 20
        b = 0.2
        c = 2 * math.pi

        for i in range(0, self.dim):
            left_sum += location[i]**2
            right_sum += math.cos(c * location[i])
        

        return (-a * math.exp(-b * math.sqrt(left_sum / self.dim)) - 
                math.exp(right_sum / self.dim) + a + math.exp(1))

    
    # The following function evaluates the n-dimensional location argument value
    # when plugged into the Sphere function as defined here:
    # https://www.sfu.ca/~ssurjano/spheref.html
    def eval_sphere(self, location):
        acc = 0

        for i in range(self.dim):
            acc += location[i] ** 2
        
        return acc
