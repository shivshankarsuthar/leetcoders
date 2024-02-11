from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = len(nums) * (len(nums)+1) / 2
        listSum = 0
        for i in nums:
            listSum += i
        missingOne = int(sum - listSum)
        return missingOne
    
    def missingNumberWithXor(self,nums):
        result = 0
        for i in range(len(nums)):
            result = result ^ i ^ nums[i]
        result = result ^ len(nums) 
        return result
#print(Solution().missingNumber([2,1]))
print(Solution().missingNumberWithXor([1,3,2,4,6,7,8,0]))