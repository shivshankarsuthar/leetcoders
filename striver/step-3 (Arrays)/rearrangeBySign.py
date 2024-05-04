from typing import *

def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    positives = []
    negatives = []
    for number in a:
        if number > 0:
            positives.append(number)
        if number < 0:
            negatives.append(number)
    result = []
    for a,b in zip(positives,negatives):
        result.append(a)
        result.append(b)
    return result


print(alternateNumbers([1,2,-4,-5]))