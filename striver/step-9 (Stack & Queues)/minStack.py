minimum = 100000000000
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        global minimum
        if minimum > val:
            self.stack.append(minimum)
            minimum = val
        self.stack.append(val)

    def pop(self) -> None:
        global minimum
        if len(self.stack) > 0:
            if minimum == self.stack.pop():
                minimum = self.stack.pop()
        return -1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        global minimum
        return minimum 
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
    
stack = MinStack()
stack.push(-1)
stack.top()
print(stack.getMin())