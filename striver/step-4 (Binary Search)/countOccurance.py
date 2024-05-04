def count(arr: [int], n: int, x: int) -> int:
	# Write Your Code Here
    l = 0
    r = n - 1
    firstIndex = None
    while l <= r:
        m = (l+r)//2
        if arr[m] == x:
            firstIndex = m
            r = m - 1
        elif arr[m] > x:
            r = m - 1
        else:
            l = m + 1

    l = 0
    r = n - 1
    lastIndex = None
    while l <= r:
        m = (l+r)//2
        if arr[m] == x:
            lastIndex = m
            l = m + 1
        elif arr[m] > x:
            r = m - 1
        else:
            l = m + 1

    if firstIndex is None or lastIndex is None:
        return 0
    return (lastIndex-firstIndex+1)

print(count([1,2,4,6,6,6,7,8],8,3))