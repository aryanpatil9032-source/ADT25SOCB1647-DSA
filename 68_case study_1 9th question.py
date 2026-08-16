stack = []
MAX_REPORTS = 25

def push(report_no, status):
    if len(stack) >= MAX_REPORTS:
        print("Stack is full")
        return

    if status != "Pending":
        print("Only pending reports can be added")
        return

    for report in stack:
        if report[0] == report_no:
            print("Report number already exists")
            return

    stack.append((report_no, status))
    print("Report added")

def pop():
    if not stack:
        print("No reports")
        return

    print("Reviewed:", stack.pop())

def peek():
    if not stack:
        print("No reports")
    else:
        print("Latest report:", stack[-1])

def display():
    if not stack:
        print("No reports")
    else:
        for report in reversed(stack):
            print(report)

push(101, "Pending")
push(102, "Pending")
push(103, "Completed")

display()
peek()
pop()
display()
