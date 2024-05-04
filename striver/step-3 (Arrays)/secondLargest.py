def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    l = 0
    r = n-1
    minimum = 1000000000
    maximum = -1
    secondMinimum = 10000000000
    secondMaximum = -1
    for i in range(len(a)):
        if a[i] < minimum:
            minimum = a[i]
        elif a[i] < secondMinimum:
            secondMinimum = a[i]
        if a[i] > maximum:
            maximum = a[i]
        elif a[i] > secondMaximum:
            secondMaximum = a[i]
    
    return [secondMaximum,secondMinimum]

print(getSecondOrderElements(5,[1,2,3,4,5]))
