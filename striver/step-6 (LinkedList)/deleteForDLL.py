class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Do not change code above.


def deleteLastNode(head: Node) -> Node:
    # Write your code here
    current = head
    if current.next is None or current is None:
        return None
    
    while current.next.next != None:
        current = current.next
    current.next.prev = None
    current.next = None
    return head    
