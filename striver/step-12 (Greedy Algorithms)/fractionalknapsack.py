class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w




class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        # code here
        arr.sort(key = lambda x:(x.value/x.weight),reverse=True)
        consumedWeight = 0
        earnedValue = 0
        for i in range(len(arr)):
            if consumedWeight + arr[i].weight > w:
                earnedValue += (w-consumedWeight) * arr[i].value / arr[i].weight
                break
            else:
                consumedWeight += arr[i].weight
                earnedValue += arr[i].value
        return earnedValue



arr = [Item(60,10),Item(100,20),Item(120,30)]
print(Solution().fractionalknapsack(50,arr,len(arr)))
