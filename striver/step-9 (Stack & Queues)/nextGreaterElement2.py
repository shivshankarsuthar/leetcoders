from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        hashMap = {}
        stack = []
        nums += nums
        for i in range(len(nums)):
            while len(stack) > 0 and stack[-1] < nums[i]:
                hashMap[stack.pop()] = nums[i]
            stack.append(nums[i])
        result = []
        for i in range(len(nums)//2):
            if nums[i] in hashMap:
                result.append(hashMap[nums[i]])
            else:
                result.append(-1)
        return result
print(Solution().nextGreaterElements([1,2,3,4,3]))