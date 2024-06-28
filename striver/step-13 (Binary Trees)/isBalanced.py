#Definition for a binary tree node.
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeTraversel(root,depth):
    if root is None:
        return depth
    
    leftDepth = treeTraversel(root.left,depth+1)
    rightDepth = treeTraversel(root.right,depth+1)
    if leftDepth is False or rightDepth is False:
        return False
    
    if abs(leftDepth-rightDepth) <= 1:
        return max(leftDepth,rightDepth)
    else:
        return False
    
class Solution:
    def isBalanced(self, root):
        return False if treeTraversel(root,0) is False else True       


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.right.right.right = BinaryTreeNode(8)

print(Solution().isBalanced(root))