from typing import List

dp = []
answer = 0
class Solution:
    def totalSubarray(self,nums,k,l,r):
        global dp,answer
        if l > r or l < 0 or r > len(nums)-1:
            return
      
        if dp[l][r] != -1:
            localSum = dp[l][r]
         
        else:
            localSum = sum(nums[l:r+1])
            dp[l][r] = localSum
        if localSum == k:
            answer += 1
        self.totalSubarray(nums,k,l+1,r)
        self.totalSubarray(nums,k,l,r-1)
        

    def subarraySum(self, nums: List[int], k: int) -> int:
        global answer,dp
        for i in range(len(nums)+1):
            temp = []
            for j in range(len(nums)+1):
                temp.append(-1)
            dp.append(temp)

        self.totalSubarray(nums,k,0,len(nums)-1)
        return answer
    
print(Solution().subarraySum([1,1,1],2))