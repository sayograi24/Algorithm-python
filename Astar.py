from queue import PriorityQueue

class Node:
    def __init__(self, state, g, h, parent=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

    def get_path(self):
        path = []
        current = self
        while current:
            path.append(current.state)
            current = current.parent
        return path[::-1]

def a_star_search(start_state, goal_state, heuristic):
    start_node = Node(start_state, 0, heuristic[start_state])
    frontier = PriorityQueue()
    frontier.put(start_node)
    explored = set()

    while not frontier.empty():
        current_node = frontier.get()

        if current_node.state == goal_state:
            return current_node.get_path()

        explored.add(current_node.state)

        for neighbor in expand(current_node.state):
            g = current_node.g + 1
            h = heuristic.get(neighbor, float('inf'))
            neighbor_node = Node(neighbor, g, h, current_node)

            if neighbor not in explored:
                frontier.put(neighbor_node)

    return None

def expand(state):
    return [f"{state}-{i}" for i in range(1, 4)]

if __name__ == "__main__":
    heuristic = {
        "A": 6,
        "A-1": 5,
        "A-2": 4,
        "A-3": 3,
        "A-1-1": 4,
        "A-1-2": 2,
        "A-2-1": 2,
        "A-2-2": 1,
        "A-3-1": 2,
        "A-3-2": 0,
        "A-3": 0
    }

    start = "A"
    goal = "A-3-2"
    result_path = a_star_search(start, goal, heuristic)

    if result_path:
        print("Goal found!")
        print("Path to goal:", " -> ".join(result_path))
    else:
        print("Goal not found.")
