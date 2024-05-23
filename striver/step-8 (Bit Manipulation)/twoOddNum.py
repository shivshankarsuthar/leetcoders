#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        xor = Arr[0]
        for num in Arr[1:]:
            xor ^= num
        setBit = xor & -xor
        xGroup = 0
        yGroup = 0
        for num in Arr:
            if num & setBit:
                xGroup ^= num
            else:
                yGroup ^= num
        return [max(xGroup,yGroup),min(xGroup,yGroup)]
    
print(Solution().twoOddNum([1,2,2,2,5,1,5,7],8))
