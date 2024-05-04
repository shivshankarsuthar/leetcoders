from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                    return m
            elif nums[m] >= nums[l]:
                if nums[l] <= target and nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target and nums[r] >= target:
                    l = m + 1
                else:
                    r = m - 1
        return -1
    
print(Solution().search([3,1],1))