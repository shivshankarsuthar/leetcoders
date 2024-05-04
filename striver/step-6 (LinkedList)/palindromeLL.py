# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printLL(self,node):
        while node!= None:
            print(node.val)
            node = node.next

    def isPalindrome(self, head) -> bool:
        if head.next == None:
            return True
        
        slow = head
        fast = head
        prev = None
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        while slow != None:
            after = slow.next
            slow.next = prev
            prev = slow
            slow = after
        r = prev
        l = head
        while l != None and l != r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = None
print(Solution().isPalindrome(head))