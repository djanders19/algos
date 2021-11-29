# This class represents an "Agent" - some type of many-dimensional entity that
# is initialized to an n-dimensional location and attempts to explore the
# space it is in in a way defined by a Strategy. This Strategy could be
# hill-climbing/gradient ascent/descent, Randomized hill climbing, just a plain
# ol' random walk, or something fancier like Simulated Annealing.

class Agent:
    def __init__(self, problem, initial_state, strategy):
        this.problem = problem
        this.state = initial_state
        this.strategy = strategy