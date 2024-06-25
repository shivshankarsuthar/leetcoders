from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                count += 1
        if sum(nums) == len(nums):
            return count
        else:
            return -1

print(Solution().minOperations([0,1,1,1]))