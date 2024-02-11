from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tracker = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[tracker] = nums[tracker],nums[i]
                tracker += 1

        print(nums)
Solution().moveZeroes([1,4,0,2,0,3,0,0,75,3])