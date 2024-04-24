# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head is None or head.next is None:
            return None
        l = head
        r = head
        i = 0
        while i < n:
            r = r.next
            i += 1
        while r != None:
            if r.next == None:
                l.next = l.next.next
                return head
            l = l.next
            r = r.next
        if r == None:
            return head.next
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(0)
# head.next.next.next.next = ListNode(1)
# head.next.next.next.next.next = ListNode(3)
# head.next.next.next.next.next.next = None
head = Solution().removeNthFromEnd(head,3)
current = head
while current != None:
    print(current.val)
    current = current.next