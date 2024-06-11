from typing import List

def atmost(nums,k):
    if k < 0 :
        return 0
    count = 0
    i = 0
    for j in range(len(nums)):
        if nums[j] & 1:
            k -= 1
        while k < 0:
            if nums[i] & 1:
                k += 1
            i += 1
        count += j - i + 1
    return count

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return atmost(nums,k) - atmost(nums,k-1)
    
print(Solution().numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],2))