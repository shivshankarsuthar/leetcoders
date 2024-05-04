class Solution:
    def frequencySort(self, s: str) -> str:
        hashMap = {}
        for ch in s:
            if ch not in hashMap:
                hashMap[ch] = 1
            else:
                hashMap[ch] += 1
        orderedList = sorted(hashMap.items(),key=lambda x:x[0])
        orderedList = sorted(orderedList,key=lambda x:x[1],reverse=True)

        result = ''
        for item in orderedList:
            result += item[0] * item[1]
        return result
    
print(Solution().frequencySort('Aabb'))