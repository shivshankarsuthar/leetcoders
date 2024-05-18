from typing import List
from copy import deepcopy
returnList = []

def combinationSumUtil(candidates,target,n,result):
    global returnList
    if n <= 0:
        return 
    if target < 0:
        return
    if target == 0:
        if result[:] not in returnList:
            returnList.append(result[:])

    result.append(candidates[n-1])
    combinationSumUtil(candidates,target-candidates[n-1],n,result)
    result.pop()
    combinationSumUtil(candidates,target,n-1,result)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        global returnList
        result = []
        combinationSumUtil(candidates,target,len(candidates),result)
        return returnList

print(Solution().combinationSum([2,3,5],8))