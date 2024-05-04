from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        ans = -1
        while l <= r:
            m = (l+r)//2
            Sum = 0
            for x in nums:
                Sum += math.ceil(x / m) 
            if Sum <= threshold:
                r = m - 1
                ans = m
            else:
                l = m + 1
        return ans
    
print(Solution().smallestDivisor([44,22,33,11,1],5))