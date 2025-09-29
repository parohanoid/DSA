# Given an integer array nums and an integer k, write a function to identify the highest possible sum of a subarray within nums, where the subarray meets the following criteria: its length is k, and all of its elements are unique.

# Example 1: Input:

nums = [3, 2, 2, 3, 4, 6, 7, 7, -1]
k = 4
# Output:

# 20

def uniq_sum_subarray(arr):
    # make the window
    # expand and sum and max sum until window is valid
    # when there is duplicate number, replace start of the window with current index, reset the set, reset the current window sum to the current num
    # keep expanding and max summing

    l = 0
    res = 0
    seen = set()
    win_sum = 0
    for i, n in enumerate(arr):
        if (n in seen):
            l = i
            seen.clear()
            win_sum = 0

        if len(seen) == k:
            win_sum -= arr[l]
            seen.discard(arr[l])
            l += 1
        
        win_sum += n
        seen.add(n)
        res = max(res, win_sum)
    return res

print(uniq_sum_subarray(nums))
