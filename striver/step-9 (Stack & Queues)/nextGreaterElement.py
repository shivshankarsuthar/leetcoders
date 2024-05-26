from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) == 1:
            return [-1]
        hashMap = {}
        stack = []
        for i in range(len(nums2)):               
            while len(stack) > 0 and stack[-1] < nums2[i]:
                hashMap[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] in hashMap:
                nums1[i] = hashMap[nums1[i]]
            else:
                nums1[i] = -1
        return nums1
    

print(Solution().nextGreaterElement([4,1,2],[1,3,4,2]))