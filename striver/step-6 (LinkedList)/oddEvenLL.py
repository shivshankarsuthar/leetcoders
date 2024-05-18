# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        oddHead = head
        evenHead = head.next
        odd = oddHead
        even = evenHead
        while (odd != None and odd.next != None and odd.next.next != None) or (even != None and even.next != None and even.next.next != None):
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead
        return head
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next = None
head = Solution().oddEvenList(head)
current = head
while current != None:
    print(current.val)
    current = current.next