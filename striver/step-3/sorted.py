from typing import List


def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    element = a[0]
    for i in range(len(a)):
        if a[i] < element:
            return 0
        else:
            element = a[i]
    return 1    

class Solution:
    def check(self, nums: List[int]) -> bool:
        k = 0
        temp = nums[0]
        for i in range(len(nums)+1):
            if nums[i % len(nums)] < temp:
                k += 1
            
            temp = nums[i % len(nums)]
            if k > 1:
                return False
        return True
            

    
#print(isSorted(5,[1,2,3,3,5]))
print(Solution().check([3,4,5,1,2]))
