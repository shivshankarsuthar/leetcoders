from typing import List

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    hashMap = {}
    for i in v:
        hashMap[i] = 0
    for i in v:
        hashMap[i] += 1

    minFreq = 10000000000
    maxFreq = 0
    maxFreqNumber = None
    minFreqNumber = None
    for key,value in hashMap.items():
        if value > maxFreq:
            maxFreq = value
            maxFreqNumber = key
        elif value == maxFreq and key < maxFreqNumber:
            maxFreqNumber = key
        if value < minFreq:
            minFreq = value
            minFreqNumber = key
        elif value == minFreq and key < minFreqNumber:
            minFreqNumber = key
    return [maxFreqNumber,minFreqNumber]

print(getFrequencies([10,10,10,3,3,3]))