"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List

def partition(arr,low,high):
	pivot = arr[high]
	i = low-1
	j = low
	for j in range(low,high):
		if arr[j] < pivot:
			i += 1
			arr[j],arr[i] = arr[i],arr[j]
	arr[i+1],arr[high] = arr[high],arr[i+1]
	return i+1

def quickSort(arr: List[int], startIndex: int, endIndex: int):
	if startIndex >= endIndex:
		return
	pivotIndex = partition(arr,startIndex,endIndex)
	quickSort(arr,startIndex,pivotIndex-1)
	quickSort(arr,pivotIndex+1,endIndex)

arr = [2,13,4,1,28,6,3]
quickSort(arr,0,6)
print(*arr)