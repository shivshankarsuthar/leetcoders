# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def constructLL(arr) -> ListNode:
# Write your code here
    root = None
    for i in range(len(arr)-1,-1,-1):
        root = insertNode(root,arr[i])
    return root

def insertNode(root,item):
    node = ListNode(item)
    node.next = root
    root = node
    return root
    
class Solution:

    
    def reverseList(self, head):
        current = head
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev