#Definition for a binary tree node.
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

hashMap = {}

def DFSTraversal(root,row,col):
    global hashMap
    if root is None:
        return
    
    

    DFSTraversal(root.left,row+1,col-1)
    if (row,col) in hashMap:
        hashMap[(row,col)].append(root.val)
    else:
        hashMap[(row,col)] = [root.val]
    DFSTraversal(root.right,row+1,col+1)

class Solution:
    
    def verticalTraversal(self, root):
        global hashMap
        hashMap = {}
        DFSTraversal(root,0,0)
        ans = []
        hashMapList = list(hashMap.items())
        for i in range(len(hashMapList)):
            if i >= 1 and hashMapList[i][0][1] == hashMapList[i-1][0][1]:
                if hashMapList[i][0][0] < hashMapList[i-1][0][0]:
                    ans[-1] = sorted(hashMapList[i][1]) + ans[-1]
                else:
                    ans[-1] = ans[-1] + sorted(hashMapList[i][1])
            else:
                ans.append(sorted(hashMapList[i][1]))
        return ans

root = BinaryTreeNode(0)
root.right = BinaryTreeNode(1)
root.right.left = BinaryTreeNode(2)
root.right.right = BinaryTreeNode(3)
root.right.right.left = BinaryTreeNode(4)
root.right.right.right = BinaryTreeNode(5)
print(Solution().verticalTraversal(root))