from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        stack = []
        n = len(nums)
        ple = [-1] * n
        nle = [n] * n
        pge = [-1] * n
        nge = [n] * n
        for i in range(n):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                nle[stack.pop()] = i
            if len(stack) > 0:
                ple[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(n):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                nge[stack.pop()] = i
            if len(stack) > 0:
                pge[i] = stack[-1]
            stack.append(i)
 
        maxSum = 0
        minSum = 0
        for i in range(n):
            minSum += (i - ple[i]) * (nle[i] - i) * nums[i]
            maxSum += (i - pge[i]) * (nge[i] - i) * nums[i]
        return maxSum - minSum

print(Solution().subArrayRanges([4,-2,-3,4,1]))
        