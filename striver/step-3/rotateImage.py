from typing import List
import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
               matrix[j][len(matrix)-1-i] =  matrix[i][j]


Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])