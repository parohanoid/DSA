nums = [1,0,0]



for i in range(len(nums)-1, -1, -1):
    if nums[i] == 0:
        del nums[i]
        nums.append(0)

print(nums)