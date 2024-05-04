from typing import *

dp = None
def isSubsetPresentUtil(n,k,a):
    global dp
    if k == 0:
        return True
    if n == 0:
        return False
    if k < 0:
        return False
    
    if dp[n][k] != -1:
        return dp[n][k]
    else:
        dp[n][k] = isSubsetPresentUtil(n-1,k-a[n-1],a) or  isSubsetPresentUtil(n-1,k,a)
        return dp[n][k]


def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    global dp
    # Write your code here.
    dp = [[-1]*(k+1)]*(n+1)

    return isSubsetPresentUtil(n,k,a)

print(isSubsetPresent(3,9,[35,1,20]))