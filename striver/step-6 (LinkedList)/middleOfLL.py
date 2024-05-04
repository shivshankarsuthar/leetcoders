# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        current = head
        middle = head
        length = 0
        while current != None:
            length += 1
            if length % 2 == 0:
                middle = middle.next
            current = current.next
        return middle