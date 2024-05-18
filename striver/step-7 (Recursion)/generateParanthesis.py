from typing import List

def generateParenthesisUtil(result,string,open,close,n):
    if len(string) >= n*2:
        result.append(string)
        return
    
    if open < n:
        generateParenthesisUtil(result,string+'(',open+1,close,n)
    if open > close:
        generateParenthesisUtil(result,string+')',open,close+1,n)
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        generateParenthesisUtil(result ,'',0,0,n)
        return result

print(Solution().generateParenthesis(3))