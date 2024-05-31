class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        # Code here
        result = []
        for index in indices:
            count = 0
            for i in range(index+1,len(arr)):
                if arr[i] > arr[index]:
                    count += 1
            result.append(count)
        return result
    
print(Solution().count_NGEs(8,[3,4,2,7,5,8,10,6],2,[0,5]))