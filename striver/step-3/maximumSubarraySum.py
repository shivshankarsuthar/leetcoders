from cmath import inf
from sys import maxsize
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        maxSum = -inf
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxSum:
                r = i
            maxSum = max(maxSum,sum)
            if sum < 0:
                sum = 0
                if i < len(nums)-1:
                    l = i + 1
        print(l,r)
        return maxSum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))