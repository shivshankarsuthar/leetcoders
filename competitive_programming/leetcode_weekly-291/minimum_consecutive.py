from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashMap = {}
        i = 0
        minimum = 10000000
        for j in range(len(cards)):
            hashMap[cards[j]] = [0,-1]

        for j in range(len(cards)):
            if hashMap[cards[j]][0] == 1:
                minimum = min(minimum,j-hashMap[cards[j]][1]+1)
        
            hashMap[cards[j]][0] +=  1
            hashMap[cards[j]][1] = j
        return minimum if minimum != 10000000 else -1
    
print(Solution().minimumCardPickup([70,37,70,41,1,62,71,49,38,50,29,76,29,41,22,66,88,18,85,53]))
