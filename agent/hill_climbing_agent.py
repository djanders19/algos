from agent.agent import Agent


class HillClimbingAgent(Agent):
    
    def __init__(self, function_type, initial_state, step_size):
        super(HillClimbingAgent, self).__init__(function_type, initial_state)
        self.step_size = step_size

    # Internal function that finds the optimal step from current agent location.
    # Upon finding the best step, it updates the current location.
    def _step(self):
        bestSoFar = self.state
        diff = 0

        for i in range(self.dimensions):
            # Test the value of incrementing each dimension by stepsize
            localState = self.state.copy()
            localState[i] += self.step_size
            localDiff = self.value - self.eval(localState)

            # If there's a steeper step than the best so far, we want to take it
            if (localDiff > diff):
                bestSoFar = localState.copy()
                diff = localDiff
            
            # Repeat, but decrementing in the dimension:
            localState = self.state.copy()
            localState[i] -= self.step_size
            localDiff = self.value - self.eval(localState)

            if (localDiff > diff):
                bestSoFar = localState.copy()
                diff = localDiff
        
        self.state = bestSoFar.copy()
        self.value = self.eval(self.state)
        self.path.append((self.state.copy(), self.value))
    
    # Run the Hill Climbing algorithm without a specified stopping point
    def run(self):
        while True:
            curr_state = self.state.copy()
            self._step()
            if self.state == curr_state:
                # self.print_state()
                return

    # Run the hill-climbing algorithm for the specified number of iterations
    def run_for_n_iterations(self, iterations):
        for _ in range(iterations):
            curr_state = self.state.copy()
            self._step()
            if self.state == curr_state:
                # self.print_state()
                return
        self.print_state()
        return
