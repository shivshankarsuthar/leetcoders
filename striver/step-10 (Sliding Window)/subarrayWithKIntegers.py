from typing import List


class Solution:
    def atMost(self,nums,k):
        hashMap = {}
        count = 0
        i = 0
        for j in range(len(nums)):
            hashMap[nums[j]] = hashMap.get(nums[j],0) + 1
            while len(hashMap.keys()) > k:
                hashMap[nums[i]] -= 1
                if hashMap[nums[i]] == 0:
                    del hashMap[nums[i]]
                i += 1
            count += j - i + 1
        return count
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums,k) - self.atMost(nums,k-1)

print(Solution().subarraysWithKDistinct([1,2,1,2,3],2))