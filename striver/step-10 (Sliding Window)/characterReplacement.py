class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        i = 0
        hashMap = {}
        maximum = 0
     
        for j in range(i,len(s)):
            hashMap[s[j]] = hashMap.get(s[j],0) + 1
            maximum = max(maximum,hashMap[s[j]])
            while j - i + 1 - maximum > k:
                hashMap[s[i]] -= 1
                maximum = max(hashMap.values())
                i += 1
            ans = max(ans,j-i+1)
        
        return ans
    
print(Solution().characterReplacement('AAAA',2))
