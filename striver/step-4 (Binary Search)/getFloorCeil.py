def getFloorAndCeil(a, n, x):
    # Write your code here.
    l = 0
    r = len(a) - 1
    ans = r + 1
    while l <= r:
        m = (l+r)//2
        if a[m] > x:
            ans = m
            r = m - 1
        elif a[m] < x:
            l = m + 1
        else:
            return [a[m],a[m]]
    
    if ans == 0:
        return [-1,a[0]]
    elif ans ==  n:
        return [a[n-1],-1]
    else:
        return [a[ans-1],a[ans]]
        

print(getFloorAndCeil([3,4,7,8,8,10],6,9))