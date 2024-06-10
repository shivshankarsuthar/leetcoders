from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = {0:1}
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if (sum - goal) in prefixSum:
                count += prefixSum[sum-goal]
            prefixSum[sum] = prefixSum.get(sum,0) + 1
        return count
    
print(Solution().numSubarraysWithSum([0,0,0,0,0],0))