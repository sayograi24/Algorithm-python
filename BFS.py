from collections import deque

class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, n):
        new_node = Node(n)
        if self.is_empty():
            self.head = new_node
        else:
            ptr = self.head
            prev = None
            while ptr:
                prev = ptr
                if new_node.data > ptr.data:
                    ptr = ptr.right
                else:
                    ptr = ptr.left
            if new_node.data > prev.data:
                prev.right = new_node
            else:
                prev.left = new_node

    def bfs(self):
        if self.head is None:
            return
        queue = deque([self.head])

        while queue:
            current = queue.popleft()
            self.visit(current)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    @staticmethod
    def visit(node):
        print(node.data, end=", ")

    def search(self, el):
        ptr = self.head
        lvl = 0
        while ptr:
            if el == ptr.data:
                print(f"{el} Found at level {lvl}!")
                return ptr
            elif el > ptr.data:
                ptr = ptr.right
            else:
                ptr = ptr.left
            lvl += 1
        print(f"{el} Not Found!")
        return None

if __name__ == "__main__":
    ob = Tree()

    # Insert numbers using user input
    while True:
        user_input = input("Enter a number for BFS (or type 'done' to stop): ")
        if user_input.lower() == 'done':
            break
        try:
            ob.insert(int(user_input))
        except ValueError:
            print("Please enter a valid integer or 'done' to stop.")

    print("BFS: ", end="")
    ob.bfs()
    print()

    # Optional: Perform search
    search_number = int(input("Enter a number to search: "))
    ob.search(search_number)
