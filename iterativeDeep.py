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

def depth_limited_search(node, goal, depth):
    if node.state == goal:
        return node
    if depth <= 0:
        return None

    for child in expand(node):
        result = depth_limited_search(child, goal, depth - 1)
        if result:
            return result
    return None

def expand(node):
    children = []
    for i in range(1, 4):
        child_state = f"{node.state}-{i}"
        child_node = Node(child_state, parent=node)
        children.append(child_node)
    return children

def iterative_deepening_search(start_state, goal):
    depth = 0
    while True:
        print(f"Depth: {depth}")
        root_node = Node(start_state)
        result = depth_limited_search(root_node, goal, depth)
        if result:
            return result
        depth += 1

if __name__ == "__main__":
    start = "A"
    goal = "A-3"
    result_node = iterative_deepening_search(start, goal)

    if result_node:
        print("Goal found!")
        print("Path to goal:", " -> ".join(result_node.get_path()))
    else:
        print("Goal not found.")
