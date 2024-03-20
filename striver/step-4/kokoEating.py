import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxElement = max(piles)
        for i in range(1,maxElement+1):
            totalHours = 0
            for pile in piles:
                takenHour = math.ceil(pile/i)
                totalHours += takenHour
            if totalHours == h:
                return i
            
print(Solution().minEatingSpeed([30,11,23,4,20],5))