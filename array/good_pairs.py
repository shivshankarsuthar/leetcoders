from typing import List

#O(n2) solution
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         count = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#         return count
    
# result = Solution().numIdenticalPairs([1,2,3,1,1,3])
# print(result)

#O(n) solution
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        count = 0
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 1
            else:
                count += hashmap[n]
                hashmap[n] += 1
        return count
    
result = Solution().numIdenticalPairs([1,2,3,1,1,3])
print(result)