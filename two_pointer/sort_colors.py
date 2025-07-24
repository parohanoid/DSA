nums = [2,1,2,0,1,0,1,0,1]

out = [0,0,0,1,1,1,1,2,2]

for i in range(len(nums)):
    if nums[i] == 0:
        del nums[i]
        nums.insert(0, 0)

for i in range(len(nums)-1, -1, -1):
    if nums[i] == 2:
        del nums[i]
        nums.append(2)

print(nums)