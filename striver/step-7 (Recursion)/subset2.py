from typing import List

def findSubset(nums,start,n,subset,ans):
    subset.append(ans[:])

    for i in range(start,len(nums)):
        if i > start and nums[i] == nums[i-1]:
            continue
        ans.append(nums[i])
        findSubset(nums,i+1,n,subset,ans)
        ans.pop()


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()
        findSubset(nums,0,len(nums),subset,ans)
        return subset
    
print(Solution().subsetsWithDup([1,2,2]))