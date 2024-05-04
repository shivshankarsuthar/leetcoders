'''
Following is the structure of the Node class already defined.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


def length(head) :
    #Your code goes here
    if head is None:
        return 0
    count = 0
    current = head
    while current != None:
        count += 1
        current = current.next

    return count

def insert(ptr,value):
    node = Node(value)
    if ptr is not None:
        ptr.next = node
    ptr = node
    return ptr

if __name__ == '__main__':
    head = Node(5)
    current = head
    for item in [4,12,7,12,15]:
        current = insert(current,item)
    print(length(head))