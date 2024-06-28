# Definition for a binary tree node.
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

maximum = -1000000
def getMaxSum(root):
    global maximum
    if root is None:
        return 0
    
    leftSum = getMaxSum(root.left)
    rightSum = getMaxSum(root.right)
    leftRightMax = max(leftSum,rightSum)
    maxRootLeaf = max(root.val,root.val+leftRightMax)
    maxAll = max(maxRootLeaf,root.val+leftSum+rightSum)
    maximum = max(maximum,maxAll)
    return maxRootLeaf

class Solution:
    def maxPathSum(self, root) -> int:
        global maximum
        maximum = -1000000
        getMaxSum(root)
        return maximum


root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
print(Solution().maxPathSum(root))