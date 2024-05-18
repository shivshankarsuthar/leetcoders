from cmath import inf
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        maxProfit = -inf
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]
            if prices[i] > sell:
                sell = prices[i]
            maxProfit = max(sell-buy,maxProfit)
        return maxProfit

print(Solution().maxProfit([7,1,5,3,6,4]))