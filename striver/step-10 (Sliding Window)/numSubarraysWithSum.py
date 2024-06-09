from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum = 0
        i = 0
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum == goal:
                    count += 1
                elif sum > goal:
                    break
        return count

print(Solution().numSubarraysWithSum([1,0,1,0,1],2))