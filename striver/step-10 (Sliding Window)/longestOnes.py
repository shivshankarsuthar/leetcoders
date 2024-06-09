from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        countZero = 0
        longestOnes = 0
        while j < len(nums):
            if nums[j] == 0:
                countZero += 1

            while countZero > k:
                if nums[i] == 0:
                    countZero -= 1
                i += 1
            longestOnes = max(longestOnes,j-i+1)
            j += 1
        return longestOnes
print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))