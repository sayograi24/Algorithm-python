import random

class HillClimbing:
    def __init__(self, objective_function):
        self.objective_function = objective_function

    def get_neighbors(self, current_state):
        return [current_state + step for step in [-1, 1]]

    def search(self, initial_state):
        current_state = initial_state
        current_value = self.objective_function(current_state)

        while True:
            neighbors = self.get_neighbors(current_state)
            next_state = None
            next_value = current_value

            for neighbor in neighbors:
                neighbor_value = self.objective_function(neighbor)
                if neighbor_value > next_value:
                    next_value = neighbor_value
                    next_state = neighbor

            if next_state is None:
                break

            current_state = next_state
            current_value = next_value

        return current_state, current_value

def objective_function(x):
    return -1 * (x**2) + 10 * x  # Example function: A downward-facing parabola

if __name__ == "__main__":
    hc = HillClimbing(objective_function)
    initial_state = random.randint(0, 10)
    result = hc.search(initial_state)

    print(f"Initial State: {initial_state}")
    print(f"Optimal State: {result[0]}")
    print(f"Optimal Value: {result[1]}")
