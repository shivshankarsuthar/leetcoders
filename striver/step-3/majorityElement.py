def majorityElement(v: [int]) -> int:
    # Write your code here
    hashMap = {}
    for i in range(len(v)):
        if v[i] not in hashMap:
            hashMap[v[i]] = 1
        else:
            hashMap[v[i]] += 1

    for key,value in hashMap.items():
        if value > len(v)//2:
            return key
    return -1

def majorityElementOptimised(v):
    for i in range(len(v)):
        


print(majorityElement([2,2,1,3,1,1,3,1,1]))