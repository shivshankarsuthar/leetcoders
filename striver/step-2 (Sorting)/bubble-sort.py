from typing import List

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    print(*arr)

bubbleSort([5,4,3,2,1],5)