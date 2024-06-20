class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        lastNumber = ''
        for i in range(len(number)):
            if number[i] == digit:
                if number[:i] + number[(i+1):] > lastNumber:
                    lastNumber  = number[:i] + number[(i+1):]
        return lastNumber
    

print(Solution().removeDigit("123","3"))