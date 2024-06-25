# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        ans = []
        current = root
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            node = stack.pop()
            ans.append(node.val)
            if node.right is not None:
                current = node.right
        return ans
            
        