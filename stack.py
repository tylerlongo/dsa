class Stack:
    def __init__(self):
        self.__stack = list()

    def push(self, val: int) -> None:
        self.__stack.append(val)
    
    def pop(self) -> None:
        self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1]
    
    def items(self) -> list:
        return self.__stack
    
stack = Stack()
for num in range(5):
    stack.push(num)
stack.pop()
print(stack.items())