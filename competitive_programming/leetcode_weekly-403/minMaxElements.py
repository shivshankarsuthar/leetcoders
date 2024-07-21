from curses.ascii import SO
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ans = 10000000000
        while nums:
            minimum = min(nums)
            maximum = max(nums)
            ans = min(ans,(minimum+maximum)/2)
            nums.remove(minimum)
            nums.remove(maximum)
        return ans
    
print(Solution().minimumAverage([7,8,3,4,15,13,4,1]))