from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ple = [-1]*len(arr)
        nle = [len(arr)]*len(arr)
        stack = []
        for i in range(len(arr)):
            while len(stack) > 0 and arr[stack[-1]] > arr[i]:
                nle[stack.pop()] = i
          
            if len(stack) > 0:
                ple[i] = stack[-1]
            stack.append(i)
        sum = 0
    
        for i in range(len(arr)):
            leftDistance = i - ple[i]
            rightDistance = nle[i] - i
            sum = (sum + leftDistance * rightDistance * arr[i]) % (10**9+7)
        return sum