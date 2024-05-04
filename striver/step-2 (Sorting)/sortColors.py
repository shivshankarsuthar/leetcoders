from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            j = i
            while j > 0:
                if nums[j-1] > nums[j]:
                    nums[j],nums[j-1] = nums[j-1],nums[j]
                j -= 1
        print(*nums)

Solution().sortColors([2,0,2,1,1,0])