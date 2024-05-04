from sys import *
from collections import *
from math import *

from typing import List

def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.

    def findSubsetSum(nums,n,start,tempSum,ans):
        ans.append(tempSum)
        for i in range(start,n):
            tempSum += nums[i]
            findSubsetSum(nums,n,i+1,tempSum,ans)
            tempSum -= nums[i]

    num.sort()
    ans = []
    findSubsetSum(num,len(num),0,0,ans)
    return sorted(ans)

print(subsetSum([4,5]))