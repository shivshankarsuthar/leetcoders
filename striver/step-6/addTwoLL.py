# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        current = None
        head = None
        carry = 0
        while l1 != None and l2 !=None:
            addition = l1.val + l2.val + carry
            carry = addition // 10
            node = ListNode(addition % 10)
            if current != None:
                current.next = node
                current = node
            else:
                head = node
                current = node
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            addition = l1.val + carry
            carry = addition // 10
            current.next = ListNode(addition % 10)
            current = current.next
            l1 = l1.next

        while l2 != None:
            addition = l2.val + carry
            carry = addition // 10
            current.next = ListNode(addition % 10)
            current = current.next
            l2 = l2.next

        if carry:
            current.next = ListNode(1)
        return head