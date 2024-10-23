from collections import deque

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def get_path(self):
        path = []
        current = self
        while current:
            path.append(current.state)
            current = current.parent
        return path[::-1]

def bidirectional_search(start_state, goal_state):
    if start_state == goal_state:
        return Node(start_state)

    start_frontier = deque([Node(start_state)])
    goal_frontier = deque([Node(goal_state)])
    explored_from_start = {start_state: True}
    explored_from_goal = {goal_state: True}

    while start_frontier and goal_frontier:
        if start_frontier:
            start_node = start_frontier.popleft()
            if start_node.state in explored_from_goal:
                return join_paths(start_node, start_node.state, explored_from_goal)

            for neighbor in expand(start_node):
                if neighbor.state not in explored_from_start:
                    explored_from_start[neighbor.state] = True
                    start_frontier.append(neighbor)

        if goal_frontier:
            goal_node = goal_frontier.popleft()
            if goal_node.state in explored_from_start:
                return join_paths(goal_node, goal_node.state, explored_from_start)

            for neighbor in expand(goal_node):
                if neighbor.state not in explored_from_goal:
                    explored_from_goal[neighbor.state] = True
                    goal_frontier.append(neighbor)

    return None

def join_paths(node, meeting_point, explored):
    path_from_start = node.get_path()
    path_from_goal = []
    current = meeting_point
    while current in explored:
        path_from_goal.append(current)
        current = explored[current]

    return path_from_start + path_from_goal[::-1][1:]

def expand(node):
    children = []
    for i in range(1, 4):
        child_state = f"{node.state}-{i}"
        child_node = Node(child_state, parent=node)
        children.append(child_node)
    return children

if __name__ == "__main__":
    start = "A"
    goal = "A-3"
    result_node = bidirectional_search(start, goal)

    if result_node:
        print("Goal found!")
        print("Path to goal:", " -> ".join(result_node))
    else:
        print("Goal not found.")
