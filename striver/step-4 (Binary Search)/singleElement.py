from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n-1] != nums[n-2]:
            return nums[n-1]
        l = 1
        r = n - 2
        while l <= r:
            m = (l+r)//2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            elif (nums[m] == nums[m-1] and (m - 1) % 2 == 1 and m % 2 == 0) or (nums[m] == nums[m+1] and (m+1) % 2 == 0 and m % 2 == 1):
                r = m - 1
            else:
                l = m + 1
           
        return -1
    
print(Solution().singleNonDuplicate([7,7,10,11,11,12,12]))