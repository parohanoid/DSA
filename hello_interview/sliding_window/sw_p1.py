# Write a function to return the length of the longest substring in a provided string s where all characters in the substring are distinct.

s = "eghghhgg"
# op = 3
# s = "substring"


# as per template
def uniq_substring_canonical(s):
    start = 0
    seen = {}
    max_len = 0
    for i, c in enumerate(s):
        seen[c] = seen.get(c, 0) + 1
        while seen[c] > 1:
            seen[s[start]] -= 1
            start += 1
        max_len = max(max_len, i - start + 1)
    return max_len

print(uniq_substring_canonical(s))