class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node("E201")
head.next = Node("E202")
head.next.next = Node("E203")
head.next.next.next = Node("E204")
head.next.next.next.next = Node("E205")

def display():
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

print("Employee List:")
display()

head = head.next

print("Updated List:")
display()

print("Head is now:", head.data)
