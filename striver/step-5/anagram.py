class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        for ch in s:
            if ch not in hashMap:
                hashMap[ch] = 1
            else:
                hashMap[ch] += 1
        
        for ch in t:
            if ch not in hashMap:
                hashMap[ch] = -1
            else:
                hashMap[ch] -= 1
        
        for count in hashMap.values():
            if count != 0:
                return False
        return True

print(Solution().isAnagram('rat','cat'))