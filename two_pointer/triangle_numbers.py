import itertools

nums = [11,4,9,6,15,18]
nums.sort()

possibles = itertools.combinations(nums, 3)

output = 10

count = 0

for possible in possibles:
    if (
        possible[0] + possible[1] > possible[2] and
        possible[1] + possible[2] > possible[0] and
        possible[0] + possible[2] > possible[1]
    ):
        count += 1

print(count)