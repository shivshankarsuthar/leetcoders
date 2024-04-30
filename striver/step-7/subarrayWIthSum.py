from copy import deepcopy;
def subarraysWithSumK( a, k):
    # Write your code here
    result = []
    l = 0
    r = 0
    n = len(a)
    currentSum = 0
    while r < n:
        if currentSum == k:
            result.append(a[l:r])
        currentSum += a[r]
        r += 1

        while currentSum - a[l] > k and l < r:
            currentSum -= a[l]
            l += 1
        
    return result

print(subarraysWithSumK([1,2,1,3],3))
                