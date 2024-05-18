from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m - 1
        selectedRow = -1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                selectedRow = mid
                l = mid + 1
            else:
                r = mid - 1
        
        l = 0
        r = n - 1
        while l <= r:
            mid = (l+r)//2
            if matrix[selectedRow][mid] == target:
                return True
            elif matrix[selectedRow][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

print(Solution().searchMatrix([[1,3,5,7]],7))