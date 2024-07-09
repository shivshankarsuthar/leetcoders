from curses.ascii import SO
from tabnanny import check
from typing import List

result = []
maximum = 0

def getCombinations(nums,i,n,k):
    global result,maximum
    print(i,len(result),maximum)
    if i >= n:
        maximum = max(maximum,len(result))
        return
    
    picked = False
    if len(result) >= 2:
        if (result[-2] + result[-1]) % k == (result[-1] + nums[i]) % k:
            result.append(nums[i])
            picked = True
    else:
        result.append(nums[i])
        picked = True
    
    if picked:
        getCombinations(nums,i+1,n,k)
        result.pop()
    getCombinations(nums,i+1,n,k)
    
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        global result,maximum
        result = []
        maximum = 0
        getCombinations(nums,0,len(nums),k)
        return maximum
        
print(Solution().maximumLength([1,2,3,4,5],2))