# Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.
# Example:
# Input: nums = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9
# Explanation: The subarray with the maximum sum is [5, 1, 3] with a sum of 9.

nums = [2, 1, 5, 1, 3, 2]
k = 3

def max_sum(arr):
    res = 0
    left = 0
    for i in range(k, len(arr)):
        res = max(res, sum(arr[left:i]))
        left += 1
    return res

print(max_sum(nums))