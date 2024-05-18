from typing import List


def solve(i,s,f):
    if i == len(s):
        print(f)
        return
    
    f.append(s[i])
    solve(i+1,s,f)
    f.pop()
    solve(i+1,s,f)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        n = len(nums)
        for i in range(2 ** n):
            set = []
            for j in range(n):
                if i & ( 1 << j):
                    set.append(nums[j])
            sets.append(set)
        return sets
    
    def subsetsRec(self,str):
        solve(0,str,[])


#print(Solution().subsets([1,2,3]))
Solution().subsetsRec([1,2,3])