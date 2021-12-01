# This class represents an "Agent" - some type of many-dimensional entity that
# is initialized to an n-dimensional location and attempts to explore the
# space it is in in a way defined by a Strategy. This Strategy could be
# hill-climbing/gradient ascent/descent, Randomized hill climbing, just a plain
# ol' random walk, or something fancier like Simulated Annealing.

class Agent:

    # Initialize the agent with a particular problem, an initial state, and 
    # a "strategy".
    # Strategies may be one of:
    # 1. hc - naive hill climbing
    # 2. rrhc - random restart hill climbing
    # 3. sa - simulated annealing
    def __init__(self, problem, initial_state):
        self.problem = problem
        self.state = initial_state.copy()
        self.value = self.eval(self.state)

    def print_state(self):
        print("Agent is at state: ", self.state)
        print("Value is: ", self.eval(self.state))

    def eval(self, state):
        return self.problem.eval(state)