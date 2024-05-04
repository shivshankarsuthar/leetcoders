class Node:
    def __init__(self,value=0,next=None):
        self.data = value
        self.next = next

def insertAtFirst(list: Node, newValue: int) -> Node:
    # Write your code here
    node = Node(newValue)
    node.next = list
    list = node
    return list
