class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(11)
head.next = Node(12)
head.next.next = Node(13)
head.next.next.next = Node(14)
head.next.next.next.next = Node(15)

def display():
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

print("Attendance List:")
display()

temp = head
while temp.next.next:
    temp = temp.next

temp.next = None

print("Updated List:")
display()

print("Node 14 next pointer changes to None")
