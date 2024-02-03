def mergeSort(arr: [int], l: int, r: int):
    # Write Your Code Here
     if (l>=r):
          return
     
     m = (l+r)//2
     
     mergeSort(arr,l,m)
     mergeSort(arr,m+1,r)
     print(arr[l],arr[m],arr[r])

arr = [2,13,4,1,3,6,28]
mergeSort(arr,0,len(arr)-1)