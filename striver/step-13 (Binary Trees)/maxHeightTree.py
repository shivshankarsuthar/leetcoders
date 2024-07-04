#Definition for a binary tree node.
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
def getDepth(root,depth):
    if root is None:
        return depth
    
    leftDepth = getDepth(root.left,depth+1)
    rightDepth = getDepth(root.right,depth+1)
    return max(leftDepth,rightDepth) 
    
class Solution:
    def maxDepth(self, root):
        return getDepth(root,0)
    
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
print(Solution().maxDepth(root))