class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        entry = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        return None