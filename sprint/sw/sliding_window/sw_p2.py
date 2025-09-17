# Write a function to find the length of the longest substring containing the same letter in a given string s, after performing at most k operations in which you can choose any character of the string and change it to any other uppercase English letter.
# s = "BBABCCDD"
s = "AABABBA"
k = 2
# should return 5

def longest_ss(s, k):
    max_len = 0
    start = 0
    state = {}
    for i, c in enumerate(s):
        state[c] = state.get(c, 0) + 1

        while (i - start + 1) - max(state.values()) > k:
            state[s[start]] -= 1
            start += 1
        
        max_len = max(max_len, i - start + 1)

    return max_len

print(longest_ss(s, k))
        