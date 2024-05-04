from typing import List

def findDays(weights,minWeight):
    days = 1
    totalW = 0
    for w in weights:
        totalW += w
        if totalW > minWeight:
            days += 1
            totalW = w
    return days

class Solution:
    def shipWithinDaysLinearSearch(self, weights: List[int], days: int) -> int:
        minW = max(weights)
        maxW = sum(weights)
        for i in range(minW,maxW+1):
            tookDays = findDays(weights,i)
            if tookDays <= days:
                return i
            
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = -1
        while l <= r:
            m = (l+r)//2
            if findDays(weights,m) <= days:
                r = m - 1
                ans = m
            else:
                l = m + 1
        return ans

print(Solution().shipWithinDays([3,2,2,4,1,4],3))