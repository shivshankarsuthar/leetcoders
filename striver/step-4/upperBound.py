def binarySearch(arr,l,r,x):
    ans = r + 1
    while l <= r:
        m = (l+r)//2
        if arr[m] > x:
            ans = m
            r = m - 1
        elif arr[m] < x:
            l = m + 1
        else:
            return m + 1

    return ans

def upperBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    return binarySearch(arr,0,n-1,x)
    

print(upperBound([1,4,7,8,10],5,7))