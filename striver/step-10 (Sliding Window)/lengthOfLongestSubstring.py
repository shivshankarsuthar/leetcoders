class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        substring = ''
        maxLength = 0
        while l <= r and l < len(s) and r < len(s):
            if s[r] not in substring:
                substring = s[l:r+1]
                maxLength = max(maxLength,len(substring))
            else:
                for i in range(len(s)):
                    if s[i] == s[r]:
                        l = i + 1
                        break
            r += 1
        return maxLength
    
print(Solution().lengthOfLongestSubstring('dvdf'))