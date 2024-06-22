from sys import *
from collections import *
from math import *

ans = [[],[],[]]
# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    ans[0].append(root.data)
    inOrder(root.right)

def preOrder(root):
    if root is None:
        return
    ans[1].append(root.data)
    preOrder(root.left)
    preOrder(root.right)
    
def postOrder(root):
    if root is None:
        return 
    postOrder(root.left)
    postOrder(root.right)
    ans[2].append(root.data)
    
def getTreeTraversal(root):
    # Write your code here.
    global ans
    inOrder(root)
    preOrder(root)
    postOrder(root)
    return ans
    
root = BinaryTreeNode(4)
root.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(6)
root.left.left = BinaryTreeNode(7)
root.left.right = BinaryTreeNode(8)
root.right.left = BinaryTreeNode(9)
root.right.right = BinaryTreeNode(10)
print(getTreeTraversal(root))