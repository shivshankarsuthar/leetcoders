class Solution:
    def recurresion(self,prev,current):
        if current is None:
            return prev
        temp = current.next
        current.next =  prev
        prev = current
        current = temp
        return self.recurresion(prev,current)

    def reverseList(self, head):
        prev = None
        return self.recurresion(prev,head)