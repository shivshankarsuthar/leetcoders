#Definition for a binary tree node.
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

maximum = 0
def treeTraversel(root):
    global maximum
    if root is None:
        return 0
    
    leftDepth = treeTraversel(root.left)
    rightDepth = treeTraversel(root.right)
    maximum = max(maximum,leftDepth+rightDepth)
    return max(leftDepth,rightDepth) + 1
    
class Solution:
    def diameterOfBinaryTree(self, root):
        global maximum
        maximum = 0
        treeTraversel(root)   
        return maximum

root = BinaryTreeNode(1)
root.right = BinaryTreeNode(2)


print(Solution().diameterOfBinaryTree(root))