class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        result = ''
        l = 0
        for i,parenthesis in enumerate(s):
            if parenthesis == '(':
                count += 1
            elif parenthesis == ')':
                count -= 1
            
            if count == 0: 
                if i - l > 1:
                    result += s[l+1:i]
                if i < len(s) - 1:
                    l = i + 1
        return result
    
print(Solution().removeOuterParentheses("(()())(())(()(()))"))