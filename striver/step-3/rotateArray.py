from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copyNums = nums+[]
        for i in range(len(copyNums)):
            copyNums[i] = nums[(i+k+1)%len(nums)]
        print(*copyNums)

    def rotateWithoutSpace(self,nums,k):
        for i in range(len(nums)):
            if i + k < len(nums):
                nums[i] = nums[i] * len(nums) + nums[(i+k+1) % len(nums)]
            else:
                nums[i] = nums[i] * len(nums) + nums[(i+k+1) % len(nums)] // len(nums)

        print(nums)
        for i in range(len(nums)):
            nums[i] = nums[i] % len(nums)

        print(nums)
#Solution().rotate([1,2,3,4,5,6,7],3)
Solution().rotateWithoutSpace([1,2,3,4,5,6,7],3)