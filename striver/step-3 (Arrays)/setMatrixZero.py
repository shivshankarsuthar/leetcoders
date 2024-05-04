from typing import List
import copy

class Solution:
    def setAllZeros(self,matrix,i,j):
        for k in range(len(matrix[i])):
            matrix[i][k] = 0
        for k in range(len(matrix)):
            matrix[k][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        copyMatrix = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    self.setAllZeros(copyMatrix,i,j)
        print(copyMatrix)

print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))