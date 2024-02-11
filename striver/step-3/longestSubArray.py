from typing import List

dp = []
maximum = -1

def longestSubarrayWithSumK(a: List[int], k: int,l:int,r:int) -> int:
    global maximum
    # Write your code here
    if l > r or l < 0 or r > len(a)-1:
        return
    
    if dp[l][r] != 0:
        localSum = dp[l][r]
    else:
        localSum = sum(a[l:r+1])
        dp[l][r] = localSum
    
    if localSum == k:
        maximum = max(maximum,r-l+1)
    
    longestSubarrayWithSumK(a,k,l+1,r)
    longestSubarrayWithSumK(a,k,l,r-1)
    return maximum

arr = [-1,1,1]
for i in range(len(arr)+1):
    temp = []
    for j in range(len(arr)+1):
        temp.append(0)
    dp.append(temp)
print(longestSubarrayWithSumK(arr,1,0,len(arr)-1))
