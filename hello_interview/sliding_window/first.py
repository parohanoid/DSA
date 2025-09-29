# Incrementing to sliding window

# Write a function to calculate the maximum number of fruits you can collect from an integer array fruits, where each element represents a type of fruit. You can start collecting fruits from any position in the array, but you must stop once you encounter a third distinct type of fruit. The goal is to find the longest subarray where at most two different types of fruits are collected.
# Example:
# Input: fruits = [3, 3, 2, 1, 2, 1, 0]
# Output: 4
# Explanation: We can pick up 4 fruit from the subarray [2, 1, 2, 1]

fruits = [3, 3, 2, 1, 2, 1, 0]


# naive - O(n^3)
def naive_fruits(arr):
    max_len = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if len(set(arr[i:j+1])) <= 2:
                max_len = max(max_len, j - i + 1)
            else:
                break
    return max_len

# using dict - O(n^2)
def dict_fruits(arr):
    max_len = 0
    for i in range(len(arr)):
        dict_fruit = {}
        for j in range(i, len(arr)):
            dict_fruit[arr[j]] = dict_fruit.get(arr[j], 0) + 1
            if len(dict_fruit) <= 2:
                max_len = max(max_len, j - i + 1)
            else:
                break
    return max_len

# dict as a sliding window!! - O(n)






def sw_dict(fruits):
    dict_win = {}  # fruit -> [count, last_index]
    start = 0
    max_len = 0

    for i, f in enumerate(fruits):
        if f not in dict_win:
            dict_win[f] = [0, i]
        dict_win[f][0] += 1
        dict_win[f][1] = i  # update last index

        if len(dict_win) > 2:
            # remove the fruit with the smallest last_index
            fruit_to_remove = min(dict_win, key=lambda k: dict_win[k][1])
            start = dict_win[fruit_to_remove][1] + 1
            del dict_win[fruit_to_remove]

        max_len = max(max_len, i - start + 1)

    return max_len