class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


# Please do not change code above.


def insertAtTail(head: Node, k: int) -> Node:
    # Write your code here
    if head is None:
        return Node(k)
    current = head
    while current.next != None:
        current = current.next
    current.next = Node(k,None,current)
    return head