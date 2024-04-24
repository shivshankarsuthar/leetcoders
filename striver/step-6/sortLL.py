# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(lowNode,highNode):
    i = None
    j = lowNode
    pivot = highNode
    while j != highNode:
        if j.val < pivot.val:
            i = i.next if i is not None else lowNode
            i.val,j.val = j.val,i.val
        j = j.next
    if i is not None:
        i.next.val,highNode.val = highNode.val,i.next.val
    else:
        lowNode.val,highNode.val = highNode.val,lowNode.val
    return i

def printLL(head):
    c = head
    while c is not None:
        print(c.val)
        c = c.next

def quickSort(lowNode,highNode):
    if lowNode == highNode or lowNode is None or highNode is None:
        return
    print(lowNode.val,highNode.val)
    pivotNode =  partition(lowNode,highNode)
    if pivotNode is not None and pivotNode.next is not None:
        quickSort(lowNode,pivotNode)
        quickSort(pivotNode.next.next,highNode)
        pass

class Solution:
    def sortList(self, head):
        lastNode = head
        while lastNode.next != None:
            lastNode = lastNode.next
        quickSort(head,lastNode)
        #printLL(head)       
        return head 


head = ListNode(4)
head.next = ListNode(35)
head.next.next = ListNode(100)
head.next.next.next = ListNode(111)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = None
Solution().sortList(head)