def dpMinimumEnergy(height,n):
    dp = [height[0],abs(height[1]-height[0])]
    for i in range(2,n):
        dp.append(min(abs(height[i]-dp[i-1]),abs(height[i]-dp[i-2])))
    return dp[n-1]
    
class Solution:
    def minimumEnergy(self, height, n):
        # Code here
        return dpMinimumEnergy(height,n)
    
print(Solution().minimumEnergy([10,20,30,10],3))