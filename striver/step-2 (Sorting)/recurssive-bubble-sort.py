from typing import List

def bubbleSort(arr: List[int], n: int,sortDone):
    if n > len(arr) or sortDone:
        return arr
    sortDone = True
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            sortDone = False
    return bubbleSort(arr,n+1,sortDone)

print(bubbleSort([2,13,4,1,3,6,28],0,False))