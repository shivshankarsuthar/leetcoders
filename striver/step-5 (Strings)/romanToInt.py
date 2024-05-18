class Solution:
    def romanToInt(self, s: str) -> int:
        special_dictionary = {
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        
        dictionary = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        i = 0
        result = 0
        while i < len(s):
            if i < len(s)-1 and s[i] + s[i+1] in special_dictionary:
                number = special_dictionary[s[i] + s[i+1]]
                i += 2
            else:
                number = dictionary[s[i]]
                i += 1
            result += number

        return result
    
print(Solution().romanToInt('MCMXCIV'))