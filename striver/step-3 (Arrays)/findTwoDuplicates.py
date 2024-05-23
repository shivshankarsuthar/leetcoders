from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            originalNumber = nums[i] % (n+1)
            if nums[originalNumber - 1] // (n+1) == originalNumber:
                result.append(originalNumber)
            nums[originalNumber - 1] = originalNumber * (n+1) + nums[originalNumber-1]

        return result
print(Solution().findDuplicates([1,2,1,6,5,5,3,3]))