from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        sum = 0
        i = 0
        while( i < len(nums)):
            if nums[i] >= 0:
                sum += nums[i]
            else:
                max_sum = max(sum,max_sum)
                sum = 0
            i += 1
        if max_sum == 0:
            return max(nums)
        else:
            return max_sum

result = Solution().maxSubArray([-5,-4,4,-1,2,3,-2,1])
print(result)