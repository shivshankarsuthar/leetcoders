from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        startIndex = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                startIndex = i + 1
                break
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            print(l,m,r)
            if nums[m] == target:
                return m
            if nums[startIndex] == target:
                return startIndex
            if nums[m] > target and nums[startIndex] > target:
                r = m -1
            elif nums[m] < target and nums[startIndex] > target:
                l = m + 1
                r = startIndex - 1
            elif nums[m] < target and nums[startIndex] < target:
                l = startIndex + 1
        return -1


print(Solution().searchRange([4,5,6,7,0,1,2],5))