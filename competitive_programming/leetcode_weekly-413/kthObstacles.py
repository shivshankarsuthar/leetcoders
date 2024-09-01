def dist(coord):
    return abs(coord[0]) + abs(coord[1])

class Solution:
    def resultsArray(self, queries, k: int):
        result = []
        kthDistance = -1
        smallerKthDistance = -2
        for i in range(len(queries)):
            if kthDistance <= dist(queries[i]):
                smallerKthDistance = kthDistance
                kthDistance = dist(queries[i])

            if i < k:
                if i < k-1:
                    result.append(-1)
                else:
                    result.append(kthDistance)
            else:
                if dist(queries[i]) >= kthDistance:
                    result.append(kthDistance)
                elif dist(queries[i]) < kthDistance and dist(queries[i]) > smallerKthDistance:
                    result.append(dist(queries[i]))
                else:
                    result.append(smallerKthDistance)

                
        return result

print(Solution().resultsArray([[1,2],[3,4],[2,3],[-3,0]],2))
        