def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    if int(n) != n:
        return -1
    l = 0
    r = m
    ans = 1
    while l <= r:
        mid = (l+r)//2
        multipleNumber = 1
        for _ in range(n):
            multipleNumber *= mid

        if multipleNumber == m:
            return mid
        elif multipleNumber > m:
            r = mid - 1
        else:
            l = mid + 1
    return -1

print(NthRoot(3,64))
