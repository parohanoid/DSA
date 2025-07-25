# naive O(n^2)
def naive_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                return True
    return False

# O(n)
# sorted list of nums, start from first and last
# if sum is more than target, reduce it by going left from last (right most),
# if sum is less than target, increase current sum by going right from first (left most)
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

list = [1,3,4,6,8,10,13]
target = 13

# print(two_sum(list, target))