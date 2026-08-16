queue = []
MAX_CUSTOMERS = 40

def enqueue(customer_id, has_cart):
    if len(queue) >= MAX_CUSTOMERS:
        print("Queue is full")
        return

    if not has_cart:
        print("Customer has no cart")
        return

    for customer in queue:
        if customer[0] == customer_id:
            print("Customer ID already exists")
            return

    queue.append((customer_id, has_cart))
    print("Customer added")

def dequeue():
    if not queue:
        print("Queue is empty")
        return

    print("Billed:", queue.pop(0))

def peek():
    if not queue:
        print("Queue is empty")
    else:
        print("Next customer:", queue[0])

def display():
    if not queue:
        print("Queue is empty")
    else:
        for customer in queue:
            print(customer)

enqueue(101, True)
enqueue(102, True)
enqueue(103, False)

display()
peek()
dequeue()
display()



