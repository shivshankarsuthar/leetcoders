class Stack:
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.arr = [-1]*self.size
        
    def push(self,data):
        self.arr[self.top+1] = data
        self.top += 1
        
    def pop(self):
        if self.top == -1:
            return -1
        topElement = self.arr[self.top]
        self.arr[self.top] = -1
        self.top -= 1
        return topElement
    
    def print(self):
        top = self.top
        while top != -1:
            print(self.arr[top])
            top -= 1
    
    def size(self):
        return top + 1
    
    
stack = Stack()
stack.push(4)
stack.push(5)
stack.push(6)
stack.print()
stack.pop()
stack.print()
