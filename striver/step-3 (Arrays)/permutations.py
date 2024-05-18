from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = []

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass

    def allPermutations(self,nums,index):
        if index == len(nums):
            print(nums)

        for i in range(index,len(nums)):
            nums[i],nums[index] = nums[index],nums[i]
            self.allPermutations(nums,index+1)
            #nums[i],nums[index] = nums[index],nums[i]

solution = Solution()
solution.allPermutations([1,2,3,4],0)
print(solution.result)