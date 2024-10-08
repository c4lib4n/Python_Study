class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Elemento no topo: ", stack.peek())
while not stack.is_empty():
    print(stack.pop())

