def insertionSort(arr,n):
    if n >= len(arr)-1:
        return arr
    
    j = n + 1
    while j > n and arr[j-1] > arr[j]:
        arr[j-1],arr[j] = arr[j],arr[j-1]
        j -= 1
    return insertionSort(arr,n+1)

print(insertionSort([2,1,3,4,1,3,6,28],0))