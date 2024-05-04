from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        round = 0
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        it = 0
        while it < m*n:
            while j < n - round and it < m*n:
                result.append(matrix[i][j])
                j += 1
                it += 1
            j -= 1
            i += 1
            while i < m - round and it < m*n:
                result.append(matrix[i][j])
                i += 1
                it += 1
            
            i -= 1
            j -= 1
            while j > round -1 and it < m*n:
                result.append(matrix[i][j])
                j -= 1
                it += 1
            j += 1
            i -= 1
            round += 1
            while i > round - 1 and it < m*n:
                result.append(matrix[i][j])
                i -= 1
                it += 1
            i += 1
            j += 1
        return result
        
print(Solution().spiralOrder(  [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))