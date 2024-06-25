from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 0:
                return 1
            return 0
        
        flipped = 0
        count = 0
        i = 0
        while i < len(nums):
            if i + 1 == len(nums):
                if nums[i] ^ flipped == 0:
                    count += 1
                break
            if nums[i] ^ flipped == 0 and nums[i+1] ^ flipped == 1:
                count += 2
                i += 2
            elif nums[i] ^ flipped == 0 and nums[i+1] ^ flipped == 0:
                count += 1
                i += 2
                flipped ^= 1
            else:
                i += 1
        return count 
    
print(Solution().minOperations([0,1,0,0,1]))


