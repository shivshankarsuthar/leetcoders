class Solution:
    def removeWhiteSpaces(self,s):
        i = 0
        while len(s) > 0 and s[i] == ' ':
            i += 1
        return s[i:]
    
    def removeSign(self,s):
        if s[0] == '-' or s[0] == '+':
            return s[1:]
        return s
    
    def myAtoi(self, s: str) -> int:
        if s == '':
            return 0
        s = self.removeWhiteSpaces(s)
        sign = -1 if s[0] == '-' else 1
        s = self.removeSign(s)
        integer = 0
        for ch in s:
            if ord(ch) < ord('0') or ord(ch) > ord('9'):
                break
            degit = ord(ch)-ord('0')
            integer = integer * 10 + degit
        integer = sign * integer
        if integer > 2**31 - 1:
            integer = 2**31-1
        elif integer < -2**31:
            integer = -2**31
        return integer

print(Solution().myAtoi(''))