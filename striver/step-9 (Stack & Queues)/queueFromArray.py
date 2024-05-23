class MyQueue:
    def __init__(self):
        self.size = 1000
        self.data = [-1] * self.size
        self.front = 0
        self.end = -1
        
    def push(self,x):
        self.data[self.end+1] = x
        self.end += 1
        
    def pop(self):
        if self.front > self.end:
            return -1
        frontElement = self.data[self.front]
        self.data[self.front] = -1
        self.front += 1        
        return frontElement
    
    def print(self):
        front = self.front
        while front <= self.end:
            print(self.data[front])
            front += 1
    
queue = MyQueue()
queue.push(3)
queue.push(4)
queue.push(5)
# queue.print()
print(queue.pop())
print(queue.pop())
print(queue.pop())
