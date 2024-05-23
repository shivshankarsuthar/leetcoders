#User function Template for python3

class MyQueue:
    def __init__(self) -> None:
        self.arr = []
    #Function to push an element x in a queue.
    def push(self, x):
         self.arr.append(x)
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        if len(self.arr) > 0:
            top = self.arr[0]
            self.arr = self.arr[1:]
            return top
        else:
            return -1
         # add code here
        
queue = MyQueue()
queue.push(5)
queue.push(10)
queue.push(15)
print(queue.arr)
queue.pop()
print(queue.arr)