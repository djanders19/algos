import Agent
import random as rand
import math

class SimulatedAnnealingAgent(Agent.Agent):
    def __init__(self, problem, initial_state, random_range, schedule):
        super(SimulatedAnnealingAgent, self).__init__(problem, initial_state)
        self.random_range = random_range
        self.schedule = schedule
        self.best_state_found = self.state.copy()
    
    def run(self):
        for i in range(len(self.schedule)):
            temperature = self.schedule[i]
            
            # Randomly select a successor
            elem_to_adjust = rand.randrange(0, self.problem.dim)
            temp_state = self.state.copy()
            temp_state[elem_to_adjust] += rand.uniform(-self.random_range, self.random_range)

            # Calculate Delta-E (change in energy, Value(current) - Value(next))
            delta_e = self.eval(self.state) - self.eval(temp_state)

            # if Delta-E > 0, current <- next (we move downhill)
            if (delta_e > 0):
                self.state = temp_state.copy()
                self.value = self.eval(self.state)
                if (self.value < self.eval(self.best_state_found)):
                    self.best_state_found = temp_state.copy()
            elif rand.uniform(0, 1) < math.exp(delta_e / temperature):
                # Otherwise, the move is uphill or sideways, and we want to
                # allow the move with probability e^(delta-E / T). This is 
                # what's known as the "Metropolis criterion"
                self.state = temp_state.copy()
                self.value = self.eval(self.state)

            # Lower temperature, repeat. Since temperature is specified in the
            # provided schedule, we simply repeat.
        
    def print_state(self):
        super(SimulatedAnnealingAgent, self).print_state()
        print("Best state found: ", self.best_state_found)
        print("Value is: ", self.eval(self.best_state_found))