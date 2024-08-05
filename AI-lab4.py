#program 1:
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)

s = Stack()

while True:
    user_input = int(input("Enter a number to push onto the stack (-1 to terminate): "))
    if user_input == -1:
        break
    s.push(user_input)

s.display()

print("Popping")
popped_element = s.pop()
print(f"Popped element: {popped_element}")
s.display()

print("Peeking")
top_element = s.peek()
print(f"Top element: {top_element}")

#program 2:
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)

q = Queue()

while True:
    user_input = int(input("Enter a number to enqueue onto the queue (-1 to terminate): "))
    if user_input == -1:
        break
    q.enqueue(user_input)


q.display()


print("Dequeueing")
dequeued_element = q.dequeue()
print(f"Dequeued element: {dequeued_element}")
q.display()

print("Peeking")
front_element = q.front()
print(f"Front element: {front_element}")

#program 3:
list=[6,19,17,23,38,45,77,84,90]
num=int(input("Enter a number to find: "))
loc=False
list.sort()
print(list)
low = 0
high = len(list) - 1
while low <= high:
    mid = (low + high)// 2
    if list[mid] == num:
        loc=True
        break
    elif list[mid] < num:
        low=mid+1
    elif list[mid]> num:
        high=mid-1
if loc==True:
    print(f"{num} is found at index {mid}")   
else:
    print(f"{num} is not found in list")