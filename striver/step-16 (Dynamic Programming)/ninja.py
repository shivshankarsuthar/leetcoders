#User function Template for python3
maxSum = 0

def dpMaximumPoints(arr,i,j,n,result):
    global maxSum
    if len(result) == n:
        sum = 0

        for i in range(len(result)):
            sum += arr[i][result[i]]
     
        maxSum = max(maxSum,sum)
        return
    
    if i >= n or j >= len(arr[i]):
        return
       
    if len(result) == 0 or result[-1] != j:    
        result.append(j)
        dpMaximumPoints(arr,i+1,0,n,result)
        result.pop()
  
    dpMaximumPoints(arr,i,j+1,n,result)
    
class Solution:
    def maximumPoints(self, arr, n):
        result = []
        dpMaximumPoints(arr,0,0,len(arr),result)
        return maxSum
        # Code here

print(Solution().maximumPoints([[1,2,3],[3,1,1],[3,3,3]],3))
