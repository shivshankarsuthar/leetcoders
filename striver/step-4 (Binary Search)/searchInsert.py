from typing import List 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        ans = r + 1
        while l <= r:
            m = (l+r)//2
            if nums[m] >= target:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans


print(Solution().searchInsert([1,3,5,6],0))