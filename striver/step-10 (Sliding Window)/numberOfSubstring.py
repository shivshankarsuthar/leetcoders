class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # hashmap = [0,0,0]
        # count = 0
        # i = 0
        # for j in range(len(s)):
        #     if ord(s[j]) - ord('a') < 3:
        #         hashmap[ord(s[j]) - ord('a')] += 1
        #     if hashmap[0] > 0 and hashmap[1] > 0 and hashmap[2] > 0:
        #         count += (len(s) - j - 1) * (j)
        #         hashmap = [0,0,0]
        # return count
    
print(Solution().numberOfSubstrings('abcabc'))