'''
Following is the structure of the Node class already defined.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def printLL(head):
    c = head
    while c is not None:
        print(c.data)
        c = c.next

def sortList(head):
    # Write your code here
    headOne = None
    headTwo = None
    headZero = None
    currentZero = None
    currentOne = None
    currentTwo = None
    current = head
    while current != None:
        if current.data == 0:
            if headZero is None:
                headZero = current
                currentZero = headZero
            else:
                currentZero.next = current
                currentZero = current
        elif current.data == 1:
            if headOne is None:
                headOne = current
                currentOne = headOne
            else:
                currentOne.next = current
                currentOne = current
        elif current.data == 2:
            if headTwo is None:
                headTwo = current
                currentTwo = headTwo
            else:
                currentTwo.next = current
                currentTwo = current
        current = current.next
    currentOne.next = None
    currentTwo.next = None
    currentTwo.next = None
    currentZero.next = headOne
    currentOne.next = headTwo
    return headZero

head = Node(1)
head.next = Node(0)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(0)
head.next.next.next.next.next = None
head = sortList(head)
printLL(head)
