from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            index = nums[i]
            if index >= 0 and index <= len(nums) -1:
                result.append(nums[index])
        return result
    
solution = Solution()
result = solution.buildArray([5,0,1,2,3,4])
print(result)




#Solved in 5 mins