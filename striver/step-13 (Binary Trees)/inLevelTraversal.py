# Definition for a binary tree node.
class Queue:
    def __init__(self) -> None:
        self.arr = []
        self.seek = 0

    def push(self,data):
        self.arr.append(data)

    def pop(self):
        if self.empty():
            return None
        element = self.arr[self.seek]
        self.seek += 1
        return element
    
    def empty(self):
        if len(self.arr) == self.seek:
            return True
        return False
    
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inLevelTraversal(self, root):
        queue = Queue()
        queue.push(root)
        ans = []
        while not queue.empty():
            node = queue.pop()
            ans.append(node.val)
            if node.left is not None:
                queue.push(node.left)
            if node.right is not None:
                queue.push(node.right)
        return ans
    
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
print(Solution().inLevelTraversal(root))