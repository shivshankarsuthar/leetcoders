from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        if len(cardPoints) < k:
            return -1
        
    
        totalCardSum = sum(cardPoints[:k])
        maxSum = totalCardSum
        for i in range(k-1,-1,-1):
            totalCardSum = totalCardSum - cardPoints[i] + cardPoints[len(cardPoints)  - (k - i)]
            maxSum = max(totalCardSum,maxSum)
        return maxSum
    
print(Solution().maxScore( [1,79,80,1,1,1,200,1],3))