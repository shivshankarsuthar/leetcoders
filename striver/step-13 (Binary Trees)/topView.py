# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def Traversal(root,ans,direction):
    if root is None:
        return
    if direction == 'left':
        Traversal(root.left,ans,'left')
        ans.append(root.data)
    else:
        ans.append(root.data)
        Traversal(root.right,ans,'right')
    

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        ans = []
        Traversal(root,ans,'left')
        if root.right:
            Traversal(root.right,ans,'right')
        return ans
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right  = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(Solution().topView(root))
            