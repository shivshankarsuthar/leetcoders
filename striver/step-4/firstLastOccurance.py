from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                it = m
                while it > -1 and nums[it] == nums[m] :
                    it -= 1
                firstNumber = it + 1
                it = m
                while it < len(nums) and nums[it] == nums[m]  :
                    it += 1
                secondNumber = it - 1
                return [firstNumber,secondNumber]

            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [-1,-1]

print(Solution().searchRange([],6))