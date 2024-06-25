# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

ans = []

def preOrder(root):
    if root is None:
        return
    ans.append(root.val)
    preOrder(root.left)
    preOrder(root.right)

class Solution:
    def preorderTraversal2(self, root):
        global ans
        ans = []
        preOrder(root)
        return 
    
    def preorderTraversal(self,root):
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return ans