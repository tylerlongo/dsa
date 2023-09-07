class Stack:
    def __init__(self):
        self.items = list()

    def push(self, val: int) -> None:
        self.items.append(val)
    
    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1]
    
    def getItems(self) -> list:
        return self.items
    
stack = Stack()
for num in range(5):
    stack.push(num)
stack.pop()
print(stack.getItems())