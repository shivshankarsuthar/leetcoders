from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}
        for number in nums:
            if number not in hashMap:
                hashMap[number] = 1
            else:
                hashMap[number] += 1
        for key,value in hashMap.items():
            if value == 1:
                return key
            
    def singleNumberXor(self,nums):
        result = 0
        for number in nums:
            result ^= number
        return result
            
print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumberXor([4,1,2,1,2]))