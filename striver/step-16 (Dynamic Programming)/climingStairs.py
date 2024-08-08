
# Memomization
def dpClimbStairs(dp,n):
    if n <= 2:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = dpClimbStairs(dp,n-1) + dpClimbStairs(dp,n-2)
    return dp[n]

# Tabular
def dpClimbStairsTabular(dp,n):
    for i in range(3,n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]
    
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0,1,2]
        return dpClimbStairsTabular(dp,n)
    
    
print(Solution().climbStairs(4))