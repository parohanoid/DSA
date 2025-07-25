# find triplets such that their sum is 0, ignore duplicates

from two_sum import two_sum

def threeSum(nums):
    nums = sorted(nums)
    i = 0
    result = []
    for i in range(len(nums) - 2):
        ans = two_sum(nums[i+1:], -nums[i])
        if ans:
            result.append((nums[i], nums[i+1+ans[0]], nums[i+1+ans[1]]))
    return [list(i) for i in list(set(result))]

nums = [-1,0,1,2,-1,-1]
print(threeSum(nums))