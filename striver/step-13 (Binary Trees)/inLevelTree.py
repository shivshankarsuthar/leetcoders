class BinaryNode:
    def __init__(self,data=None)
        self.data = data
        self.left = None
        self.right = None
        
class Solution:
    def insertTree(root,data):
        current = root
        while current != None:
            current = current.left
            
    def createTree(self, root, l):
        # Code here
        for i in range(len(l)):
            self.insertTree(root,l[i])