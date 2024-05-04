import math

def floorSqrt(n):
   # write your code logic here .
    l = 0
    r = n
    ans = 1
    while l <= r:
        m = (l+r)//2
        if m * m == n:
            return m
        elif m * m > n:
            r = m - 1
        else:
            ans = m
            l = m + 1
    return ans

n= int(input())
print(floorSqrt(n))