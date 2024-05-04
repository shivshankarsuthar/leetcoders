
class Node:
    def __init__(self,val=0,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

def insertNode(item,ptr):
    node = Node(item)
    node.next = ptr
    if ptr != None:
        ptr.prev = node
    ptr = node
    return ptr

def printNode(ptr):
    while ptr !=None:
        print(ptr.val)
        ptr = ptr.next


def constructDLL(arr) -> Node:
    # Write your code here
    head = None
    for i in range(len(arr)-1,-1,-1):
        head = insertNode(arr[i],head)
    return head

ptr = constructDLL([1,2,3,4,5,6])
printNode(ptr)