# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        lengthA = 0
        lengthB = 0
        current = headA
        while current is not None:
            lengthA += 1
            current = current.next
        current = headB
        while current is not None:
            lengthB += 1
            current = current.next
        diff = abs(lengthA-lengthB)
        if lengthB < lengthA:
            while diff:
                headA = headA.next
                diff -= 1
        else:
            while diff:
                headB = headB.next
                diff -= 1
        while headA != None and headB != None:
            if headB == headA:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
    def getIntersectionNode2(self, headA, headB):
        currentA = headA
        currentB = headB
        while currentA != currentB:
            currentA = currentA.next if currentA is not None else headB
            currentB = currentB.next if currentB is not None  else headA
        return currentA