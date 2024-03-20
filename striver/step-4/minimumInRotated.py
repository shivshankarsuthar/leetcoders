from math import inf
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = inf
        while l <= r:
            m = (l+r)//2           
            if nums[l] <= nums[m]:
                minimum = min(minimum,nums[l])
                l = m + 1
            else:
                minimum = min(minimum,nums[m])
                r = m - 1
        return minimum
    
print(Solution().findMin([1]))