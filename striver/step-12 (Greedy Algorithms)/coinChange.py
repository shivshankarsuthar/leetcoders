def coinChangeUtil(arr,n,v,steps):
    if n == 0 or v < 0:
        return 1000000
    if v == 0:
        return steps
    steps += 1
    leftSteps = coinChangeUtil(arr,n,v-arr[n-1],steps)
    steps -= 1
    rightSteps = coinChangeUtil(arr,n-1,v,steps)
    return min(leftSteps,rightSteps)

class Solution:
    def coinChange(self,arr,v):
        minimum =  coinChangeUtil(arr,len(arr),v,0)
        return minimum if minimum != 1000000 else -1


print(coinChange([3,7,405,436],8839))