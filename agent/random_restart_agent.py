import random as rand

from agent.agent import Agent
import agent.functions as f
from agent.hill_climbing_agent import HillClimbingAgent


class RandomRestartAgent(Agent):
    def __init__(self, function_type, initial_state, step_size, num_restarts, start_range):
        super(RandomRestartAgent, self).__init__(function_type, initial_state)
        self.step_size = step_size
        self.num_restarts = num_restarts
        self.agent = HillClimbingAgent(function_type, initial_state, step_size)
        self.start_range = start_range

    # Runs the hill-climbing algorithm, but with <self.num_restarts>
    # random restarts.
    def run(self):
        for i in range(self.num_restarts):
            # self.agent.print_state()
            # run the hill climbing agent:
            self.agent.run()

            # if the agent has found a better state, update our internals:
            if self.eval(self.agent.state) < self.value:
                self.state = self.agent.state.copy()
                self.value = self.eval(self.state)
            # keep track of the path that the agent followed:
            self.path.append(self.agent.path.copy())
            self.agent.path.clear()
            # Randomly reset the agent's starting state:
            for d in range(self.dimensions):
                self.agent.state[d] = rand.uniform(-self.start_range, self.start_range)
            self.agent.value = self.eval(self.agent.state)

    # Runs the hill climbing algorithm with <self.num_restarts> restarts,
    # limiting the number of iterations of each run of the hill-climbing
    # algorithm.
    def run_for_n_iterations(self, n):
        for i in range(self.num_restarts):
            # run the hill climbing agent:
            self.agent.run_for_n_iterations(n)

            # if the agent has found a better state, update our internals:
            if self.eval(self.agent.state) < self.value:
                self.best_state_found = self.agent.state.copy()
                self.value = self.eval(self.best_state_found)

            # Randomly reset the agent's starting state:
            for d in range(self.diminsions):
                self.state[d] = rand.uniform(-start_range, start_range)
            self.agent.value = self.eval(self.agent.state)
