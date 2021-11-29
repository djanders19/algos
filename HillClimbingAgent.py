import Agent

class HillClimbingAgent(Agent.Agent):
    
    def __init__(self, problem, initial_state, step_size):
        super(HillClimbingAgent, self).__init__(problem, initial_state)
        this.step_size = step_size

    
    # Internal function that finds the optimal step from current agent location.
    # Upon finding the best step, it updates the current location.
    def _step(self):
        bestSoFar = self.state
        diff = 0

        for i in range(self.problem.dim):
            # Test the value of incrementing each dimension by stepsize
            localState = self.state.copy()
            localState[i] += step_size
            localDiff = self.value - self.eval(localState)

            # If there's a steeper step than the best so far, we want to take it
            if (localDiff > diff):
                bestSoFar = localState.copy()
                diff = localDiff
            
            # Repeat, but decrementing in the dimension:
            localState = self.state.copy()
            localState[i] -= step_size
            localDiff = self.value - self.eval(localState)

            if (localDiff > diff):
                bestSoFar = localState.copy()
                diff = localDiff
        
        self.state = bestSoFar.copy()
        self.value = self.eval()
    
    # Run the Hill Climbing algorithm
    def run(self):



