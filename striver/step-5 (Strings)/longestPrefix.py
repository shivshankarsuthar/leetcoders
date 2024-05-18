from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestStringIndex = 0
        shortestString = 1000000000000
        for i,string in enumerate(strs):
            if len(string) < shortestString:
                shortestString = len(string)
                shortestStringIndex = i
        result = ''
        for i in range(len(strs[shortestStringIndex])):
            commonPrefixCharacterFound = True
            for string in strs:
                if string[i] != strs[shortestStringIndex][i]:
                    commonPrefixCharacterFound = False
            if commonPrefixCharacterFound:
                result += strs[shortestStringIndex][i]
            else:
                return result
                
        return result
    
print(Solution().longestCommonPrefix(["ab", "a"]))