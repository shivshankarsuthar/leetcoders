# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def postorderTraversal(self, root) -> List[int]:
        if root is None:
            return []
        stack = []
        current = root
        ans = []
        while stack or current:
            while current is not None:
                stack.append(current)
                current = current.left
            node = stack.pop()
            if node.left is None:
                ans.append(node.val)
            if node.right is not None:
                current = node.right


            