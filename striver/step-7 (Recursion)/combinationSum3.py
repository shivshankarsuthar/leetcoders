from typing import List

def findCombinationsSum(nums,k,n,i,subsets,ans):
    if n == 0 and len(subsets) == k:
        ans.append(subsets[:])
        return
    if i >= 9:
        return
    subsets.append(nums[i])
    findCombinationsSum(nums,k,n-nums[i],i+1,subsets,ans)
    subsets.pop()
    findCombinationsSum(nums,k,n,i+1,subsets,ans)

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if k * (k + 1) / 2 > n:
            return []
        
        ans = []
        subsets = []
        findCombinationsSum([1,2,3,4,5,6,7,8,9],k,n,0,subsets,ans)
        return ans
                
print(Solution().combinationSum3(9,45))