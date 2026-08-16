stack = []
MAX_BOXES = 40

def push(box_id, weight, fragile):
    if len(stack) >= MAX_BOXES:
        print("Stack is full")
        return

    if weight < 1 or weight > 50:
        print("Invalid weight")
        return

    if fragile and weight > 20:
        print("Fragile box cannot be stored")
        return

    for box in stack:
        if box[0] == box_id:
            print("Box ID already exists")
            return

    stack.append((box_id, weight, fragile))
    print("Box stored")

def pop():
    if not stack:
        print("Stack is empty")
        return

    print("Removed:", stack.pop())

def peek():
    if not stack:
        print("Stack is empty")
    else:
        print("Top box:", stack[-1])

def display():
    if not stack:
        print("Stack is empty")
    else:
        for box in reversed(stack):
            print(box)

push(101, 10, False)
push(102, 15, True)
push(103, 25, True)

display()
peek()
pop()
display()
