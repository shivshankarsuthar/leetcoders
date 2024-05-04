class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def insertNode(root,item):
    node = Node(item)
    node.next = root
    root = node
    return root

def printNodes(root):
    while root is not None:
        print(root.val)
        root = root.next


def constructLL(arr) -> Node:
    # Write your code here
    root = None
    for i in range(len(arr)-1,-1,-1):
        root = insertNode(root,arr[i])
    return root

constructLL([1,2,3,4,5])