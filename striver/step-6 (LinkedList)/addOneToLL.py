class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Don't change the code above.
def reverseLL(head):
    current = head
    prev = None
    while current != None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

def addOne(head: Node) -> Node:
    # write your code here
    head = reverseLL(head)
    current = head
    trail = 1
    prev = None
    while current != None:
        if trail == 0:
            break
        addition = current.data + trail
        current.data = addition % 10
        trail = addition // 10
        prev = current
        current = current.next
    if trail:
        prev.next = Node(1)
    head = reverseLL(head)
    return head

def printLL(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

head = Node(1)
head.next = Node(5)
head.next.next = Node(5)
head.next.next.next = None
head = addOne(head)
printLL(head)

