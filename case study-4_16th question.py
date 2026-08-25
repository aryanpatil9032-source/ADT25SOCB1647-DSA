#recursive postorder

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" -> ")

root = Node("University")
root.left = Node("Engineering")
root.right = Node("Management")
root.left.left = Node("Computer")
root.left.right = Node("Mechanical")

postorder(root)


#Non-Recursive Postorder Using Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node("University")
root.left = Node("Engineering")
root.right = Node("Management")
root.left.left = Node("Computer")
root.left.right = Node("Mechanical")

stack1 = [root]
stack2 = []

while stack1:
    node = stack1.pop()
    stack2.append(node)

    if node.left:
        stack1.append(node.left)

    if node.right:
        stack1.append(node.right)

while stack2:
    print(stack2.pop().data, end=" -> ")
