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
        new_node =  Node(n)
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
            
    def preorder(self, ptr):
        if ptr is not None:
            self.visit(ptr)
            self.preorder(ptr.left)
            self.preorder(ptr.right)
        
    def inorder(self, ptr):
        if ptr is not None:
            self.inorder(ptr.left)
            self.visit(ptr)
            self.inorder(ptr.right)

    def postorder(self, ptr):
        if ptr is not None:
            self.preorder(ptr.left)
            self.preorder(ptr.right)
            self.visit(ptr)

    @staticmethod
    def visit(node):
        print(node.data, end=", ")

    def search(self, el):
        ptr = self.head
        lvl = 0
        while ptr:
            if el == ptr.data:
                print(f"{el} found in {lvl}th level!")
                return ptr
            elif el > ptr.data:
                ptr = ptr.right
                lvl += 1
            else:
                ptr = ptr.left
                lvl += 1
        print(f"{el} not found!")
        return None

if __name__=="__main__":
    ob = Tree()

    while True:
        user_input = input("Enter a number for DFS  (or 'done' to stop):")
        if user_input.lower() == "done":
            break
        try:
            number = int(user_input)
            ob.insert(number)
        except ValueError:
            print("Please enter a valid number.")

    print("preorder: ", end="")
    ob.preorder(ob.head)
    print()
    print("inorder: ", end="")
    ob.inorder(ob.head)
    print()
    print("postorder: ", end="")
    ob.postorder(ob.head)
    print()
    
    search_value = int(input("Enter a number to search: "))
    ob.search(search_value)          

