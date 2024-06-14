from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        count = 0
        for j in range(len(g)):
            while i < len(s) and g[j] > s[i]:
                i += 1
            if i >= len(s):
                return count
            count += 1
            i += 1
        return count
    
print(Solution().findContentChildren([1,2,3],[1,1]))