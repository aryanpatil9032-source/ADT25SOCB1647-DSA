class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def recursive_preorder(root):
    if root:
        print(root.data, end=" -> ")
        recursive_preorder(root.left)
        recursive_preorder(root.right)

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

print("Recursive:")
recursive_preorder(root)

print("\nNon-Recursive:")

stack = [root]

while stack:
    node = stack.pop()
    print(node.data, end=" -> ")

    if node.right:
        stack.append(node.right)

    if node.left:
        stack.append(node.left)
