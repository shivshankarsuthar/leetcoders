from typing import List

def getCombinations(str,n,i,subsetStr,ans):
    if len(subsetStr) == n:
        ans.append(subsetStr)
        return
    if i >= len(str):
        return
    subsetStr += str[i]
    getCombinations(str,n,i+3,subsetStr,ans)
    subsetStr = subsetStr[:-1]
    getCombinations(str,n,i+1,subsetStr,ans)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        digitLetterMap = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        wholeString = ''
        lenOfDigits = 0
        for digit in digits:
            if digit in digitLetterMap:
                lenOfDigits += 1
                wholeString += digitLetterMap[digit]
        if lenOfDigits == 0:
            return []
        ans = []
        subsetStr = ''
        getCombinations(wholeString,lenOfDigits,0,subsetStr,ans)
        return ans
    
print(Solution().letterCombinations('23'))