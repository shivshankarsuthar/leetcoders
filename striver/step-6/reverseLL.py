'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
'''

def reverseDLL(head):
    # Write your code here
    if head.next is None:
        return head
    current = head
    while current != None:
        current.prev,current.next = current.next,current.prev
        if current.prev is None:
            break
        current = current.prev

    return current