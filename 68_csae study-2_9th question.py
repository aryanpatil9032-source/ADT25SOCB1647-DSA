queue = []
MAX_BOOKS = 75

def enqueue(book_id, borrowed):
    if len(queue) >= MAX_BOOKS:
        print("Queue is full")
        return

    if not borrowed:
        print("Book is not borrowed")
        return

    for book in queue:
        if book[0] == book_id:
            print("Book ID already exists")
            return

    queue.append((book_id, borrowed))
    print("Book returned")

def dequeue():
    if not queue:
        print("Queue is empty")
        return

    print("Processed:", queue.pop(0))

def peek():
    if not queue:
        print("Queue is empty")
    else:
        print("Next book:", queue[0])

def display():
    if not queue:
        print("Queue is empty")
    else:
        for book in queue:
            print(book)

enqueue(101, True)
enqueue(102, True)
enqueue(103, False)

display()
peek()
dequeue()
display()
