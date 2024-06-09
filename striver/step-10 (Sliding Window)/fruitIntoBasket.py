class Solution:
    def sumSubarrayMins(self, N, fruits):
        # Code here
        i = 0
        basket = {}
        maximum = 0
        for j in range(N):
            if len(basket.keys()) < 2 or fruits[j] in basket:
                basket[fruits[j]] = basket.get(fruits[j],0) + 1
            else:
                while len(basket.keys()) >= 2:
                    basket[fruits[i]] -= 1
                    if basket[fruits[i]] == 0:
                        del basket[fruits[i]]
                    i += 1
                basket[fruits[j]] = 1
            maximum = max(maximum,j-i+1)
        return maximum
    
print(Solution().sumSubarrayMins(22,[17 ,7, 0, 5, 11, 5, 4, 5, 12, 14, 21, 17, 11, 11, 17, 7, 8, 18, 21, 14, 16, 2]))
             