from typing import List
from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        minLen = inf
        Sum = 0

        for j in range(n):
            Sum += nums[j]
            while Sum >= target:
                minLen = min(minLen,j - i + 1)
                Sum -= nums[i]
                i += 1
               
        if minLen == inf:
            return 0
        return minLen
    
print(Solution().minSubArrayLen(7,[2,3,1,2,4,3]))