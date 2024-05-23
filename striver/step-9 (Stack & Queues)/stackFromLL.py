head = None

class StackNode:
    # # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:    
    #Function to push an integer into the stack.
    def push(self, data):
        global head
        # Add code here
        if head is None:
            head = StackNode(data)
        else:
            node = StackNode(data)
            node.next = head
            head = node

    #Function to remove an item from top of the stack.
    def pop(self):
        # Add code here
        global head
        if head is None:
            return -1
        temp = head
        head = head.next
        temp.next = None
        return temp.data
    

stack = MyStack()
stack.push(49)
print(stack.pop())
stack.push(29)
print(stack.pop())
print(stack.pop())
stack.push(69)
stack.push(23)
print(stack.pop())