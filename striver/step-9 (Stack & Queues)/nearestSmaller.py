class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack = []
        hashMap = {}
        for i in range(len(A)-1,-1,-1):
            while len(stack) > 0 and stack[-1][0] > A[i]:
                s = stack.pop()
                hashMap[(s[0],s[1])] = A[i]
            stack.append((A[i],i))
        result = []
        
        for i in range(len(A)):
            if (A[i],i) in hashMap:
                result.append(hashMap[(A[i],i)])
            else:
                result.append(-1)
        return result
    
print(Solution().prevSmaller([ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]))