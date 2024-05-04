class Solution:
    def stringMatching(self,s,goal,index):
        for i in range(len(s)):
            if s[i] != goal[index]:
                return False
            else:
                index = (index+1)%len(goal)
        return True
    
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for i in range(len(goal)):
            if s[0] == goal[i]:
                if self.stringMatching(s,goal,i):
                    return True
        return False
    
print(Solution().rotateString('bqqutquvbtgouklsayfvzewpnrbwfcdmwctusunasdbpbmhnvy','wpnrbwfcdmwctuunasdbpbmhnvybqqutquvbtgouklsayfvze'))