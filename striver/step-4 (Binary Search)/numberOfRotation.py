def findKRotation(arr : [int]) -> int:
    # Write your code here.
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r)//2
        if m < len(arr) - 1 and arr[m] > arr[m+1]:
            return m+1
        if arr[l] <= arr[m]:
            l = m + 1
        else:
            r = m - 1

    return 0

print(findKRotation([1,2,3]))
