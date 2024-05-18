class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        restructString = ''
        for character in s:
            if (character >= 'a' and character <= 'z') or (character >= '0' and character <= '9'):
                restructString += character
        if len(restructString) == 1 or len(restructString) == 0:
            return True
        i = 0
        j = len(restructString) - 1
        while i < j:
            if restructString[i] == restructString[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

print(Solution().isPalindrome("A man, a plan, a ccanal: Panama"))