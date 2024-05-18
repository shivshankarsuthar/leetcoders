class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        count = 0
        for string in s:
            if string == '(':
                count += 1
            if string == ')':
                count -= 1
            maxDepth = max(maxDepth,count)
        return maxDepth
    
print(Solution().maxDepth('(1)+((2))+(((3)))'))