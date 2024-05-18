def binarySearch(nums,l,r,target):
    if l > r:
        return -1 
    m = (l+r)//2
    if nums[m] == target:
        return m
    elif nums[m] > target:
        return binarySearch(nums,l,m-1,target)
    else:
        return binarySearch(nums,m+1,r,target)

def search(nums: [int], target: int):
    # write your code logic !!
    return binarySearch(nums,0,len(nums)-1,target)

print(search([1,3,7,9,11,12,45],453))