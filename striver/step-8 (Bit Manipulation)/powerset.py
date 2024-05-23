from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(2 ** n):
            sets = []
            for j in range(n):
                if i & (1 << j):    
                    sets.append(nums[j])
            result.append(sets)
        return result
    
print(Solution().subsets([1,2,3]))