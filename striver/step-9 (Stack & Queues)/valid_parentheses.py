class Solution:
    def __init__(self) -> None:
        self.stack = []

    def isOpen(self,ch):
        if ch == '(' or ch == '{' or ch == '[':
            return True
        return False
    
    def isClose(self,ch):
        if ch == ')' or ch == '}' or ch == ']':
            return True
        return False
    
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or self.isClose(s[0]):
            return False
        
        for ch in s:
            if self.isOpen(ch):
                self.stack.append(ch)
            else:
                if len(self.stack) > 0:
                    if (self.stack[-1] == '(' and ch == ')') or (self.stack[-1] == '{' and ch == '}') or (self.stack[-1] == '[' and ch == ']'):
                        self.stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(self.stack) > 0:
            return False
        return True
    
print(Solution().isValid('[]}'))