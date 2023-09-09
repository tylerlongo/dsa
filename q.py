class Queue:
    def __init__(self):
        self.items = list()
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.remove(self.items[0])
    
    def top(self):
        return self.items[0]
    
    def getItems(self):
        return self.items
    
q = Queue()
for i in range(5):
    q.enqueue(i)
q.dequeue()
print(q.getItems())