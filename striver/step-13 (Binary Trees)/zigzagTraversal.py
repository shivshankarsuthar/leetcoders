# Definition for a binary tree node.
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        direction = 1
        queue = [root]
        ans = []
        while queue:
            levelNodes = []
            for i in range(0,len(queue)):
                node = queue.pop(0)
                levelNodes.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            ans.append(levelNodes[::direction])
            direction *= -1
        return ans
    
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
root.left.left.left = BinaryTreeNode(8)
root.left.right.left = BinaryTreeNode(9)
root.right.right.right = BinaryTreeNode(10)
print(Solution().zigzagLevelOrder(root))