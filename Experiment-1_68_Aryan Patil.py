class Stack:
    def __init__(self):
        self.top = -1
        self.ST = [0] * 5

    def insert(self, x):
        if self.top == 4:
            print("Stack is overflow....")
            return

        self.top = self.top + 1
        self.ST[self.top] = x

    def delete(self):
        if self.top == -1:
            print("Stack is underflow....")
            return

        y = self.ST[self.top]
        self.top = self.top - 1
        return y

    def display(self):
        if self.top == -1:
            print("Nothing to print")
            return

        for i in range(self.top, -1, -1):
            print(self.ST[i])


s = Stack()

s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)
s.insert(50)
s.insert(60)

s.display()

x = s.delete()
print("Deleted:", x)

s.display()