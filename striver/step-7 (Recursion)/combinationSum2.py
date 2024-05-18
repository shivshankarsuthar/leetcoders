from typing import List
dp = {}

def combinationSum2Util(candidates,target,start,n,result,resultList):
    if target == 0:
        if result[:] not in resultList:
            resultList.append(result[:])
    for i in range(start,n):
        if i > start and candidates[i] == candidates[i-1]:
            continue
        if target - candidates[i] < 0:
            break
        result.append(candidates[i])
        combinationSum2Util(candidates,target-candidates[i],i+1,n,result,resultList)
        result.pop()
    

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        ans = []
        candidates.sort()
        combinationSum2Util(candidates,target,0,len(candidates),result,ans)
        return ans
    
print(Solution().combinationSum2([10,1,2,7,6,1,5],8))