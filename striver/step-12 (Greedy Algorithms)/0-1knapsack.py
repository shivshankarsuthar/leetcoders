class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w

maximum = -1
def chooseOrNotChoose(w,arr,n,totalValue):
    global maximum
    if n == 0:
        return
    
    if w >= 0 and w < arr[n-1].weight:
        maximum = max(maximum,totalValue)
    totalValue += arr[n-1].value
    chooseOrNotChoose(w-arr[n-1].weight,arr,n-1,totalValue)
    totalValue -= arr[n-1].value
    chooseOrNotChoose(w,arr,n-1,totalValue)


class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        # code here
        chooseOrNotChoose(w,arr,n,0)
        sum = 0
        if maximum == -1:
            for num in arr:
                sum += num.value
            return sum
        else:
            return maximum

arr = [Item(60,10),Item(100,20)]
print(Solution().fractionalknapsack(50,arr,len(arr)))
