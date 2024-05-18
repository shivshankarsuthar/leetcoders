import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = -1
        while l <= r:
            m = (l+r)//2
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile/m)
                if totalHours > h:
                    l = m + 1
                    ans = m
                    break

            if totalHours == h:
                return m
            elif totalHours <= h:
                r = m - 1
        return ans
            
print(Solution().minEatingSpeed([312884470],312884469))