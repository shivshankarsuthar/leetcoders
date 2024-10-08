from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                if abs(hashMap[nums[i]]-i) <= k:
                    return True
    
            hashMap[nums[i]] = i
        return False
    
print(Solution().containsNearbyDuplicate([1,2,3,1],3))