class Solution:
    def reverseWords(self, s: str) -> str:
        listOfString = s.split(' ')
        result = ''
        for i in range(len(listOfString)-1,-1,-1):
            if listOfString[i] != '':
                result += listOfString[i] + ' '

        return result[:-1]
    
print(Solution().reverseWords('  hello world  '))