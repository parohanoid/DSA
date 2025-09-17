from collections import defaultdict, Counter

inp = [7, 2, 9, 4, 2, 7, 1, 5, 3, 9, 6, 2, 8, 4, 7, 1, 5, 3, 8, 6]

dict_to_count = defaultdict(int)

for i in inp:
    dict_to_count[i] += 1

print(dict_to_count)

c = Counter("hello")
c.update('lo')
print(c['l'])
print(c['o'])