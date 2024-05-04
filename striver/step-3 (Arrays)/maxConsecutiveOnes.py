from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxCount = max(maxCount,count)
            elif nums[i] == 0:
                count = 0
        return maxCount

print(Solution().findMaxConsecutiveOnes([0,1,0,1,0,1]))
            
        