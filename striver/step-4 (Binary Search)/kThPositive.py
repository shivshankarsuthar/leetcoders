from typing import List


class Solution:
    def findKthPositiveLinearSearch(self, arr: List[int], k: int) -> int:
        maxNumber = arr[-1] + k
        minNumber = 1
        count = 0
        for i in range(minNumber,maxNumber+1):
            if i not in arr:
                count += 1
                if count == k:
                    return i
                
    def findKthPositive(self,arr,k):
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l+r)//2
            if arr[m] - m - 1 < k:
                l = m + 1
            else:
                r = m - 1
        return  k  + l
            
                
print(Solution().findKthPositive([1,2,3,4],2))