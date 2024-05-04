class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                if t[i] in hashMap.values():
                    return False
                hashMap[s[i]] = t[i]
            elif t[i] != hashMap[s[i]]:
                return False
            
        return True
    
print(Solution().isIsomorphic('paper','title'))