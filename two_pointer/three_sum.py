# find triplets such that their sum is 0, ignore duplicates

def two_sum(nums, target):
    i = 0
    j = len(nums) - 1 
    while i < j:
        if nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            return [i, j]
    return False


def threeSum(nums):
    nums = sorted(list(set(nums)))
    i = 0
    result = []
    for i in range(len(nums) - 2):
        ans = two_sum(nums[i+1:], -nums[i])
        if ans:
            result.append([nums[i], nums[i+1+ans[0]], nums[i+1+ans[1]]])
    return result

nums = [-1,0,1,2,-1,-1]
print(threeSum(nums))