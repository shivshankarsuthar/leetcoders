from typing import List

def getMaxima(height,l,r):
    maximum = -1
    maxima = -1
    for i in range(l+1,r):
        if maximum < height[i]:
            maxima = i
            maximum = height[i]
    return maxima

def twoPartition(height,l,r,trailingSum):
    if l+1 >= r:
        return 0
    maxima = getMaxima(height,l,r)
    if height[maxima] < height[l] and height[maxima] < height[r]:
        totalBlocks = trailingSum[r-1] - trailingSum[l]
        smallerBlock = height[l] if height[l] < height[r] else height[r]
        indexDiff = r - l - 1
        count = smallerBlock * indexDiff - totalBlocks
        return count
    return twoPartition(height,l,maxima,trailingSum) + twoPartition(height,maxima,r,trailingSum)
    
class Solution:
    def trap(self, height: List[int]) -> int:
        trailingSum = []
        sum = 0
        for i in range(len(height)):
            sum += height[i]
            trailingSum.append(sum)
        
        return twoPartition(height,0,len(height)-1,trailingSum)
    
print(Solution().trap([4,0,2,0,7,2,5]))