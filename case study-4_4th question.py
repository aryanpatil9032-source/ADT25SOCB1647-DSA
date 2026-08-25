class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node("E201")
root.left = Node("E202")
root.right = Node("E203")
root.left.left = Node("E204")
root.left.right = Node("E205")

stack = []
current = root

while current or stack:
    while current:
        stack.append(current)
        current = current.left

    current = stack.pop()
    print(current.data, end=" -> ")

    current = current.right
