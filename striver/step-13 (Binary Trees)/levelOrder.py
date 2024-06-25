# Definition for a binary tree node.
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List

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

class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if root is None:
            return []
        
        queue = Queue()
        queue.push(root)
        hashMap = {root.val:0}
        while not queue.empty():
            node = queue.pop()
            if node.left is not None:
                queue.push(node.left)
                hashMap[node.left.val] = hashMap[node.val] + 1
            if node.right is not None:
                queue.push(node.right)
                hashMap[node.right.val] = hashMap[node.val] + 1

        ans = {}
        for key,value in hashMap.items():
            if value in ans:
                ans[value].append(key)
            else:
                ans[value] = [key]
        return list(ans.values())
    
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
print(Solution().levelOrder(root))