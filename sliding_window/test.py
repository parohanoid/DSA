dict_win = {1: (0,3), 2: (0, 4)}

fruits = [3, 3, 2, 1, 2, 7, 0]

i = 5

# dict_win[fruits[i]][0] = dict_win.get(fruits[i], (0, i))[0] + 1


print(sum([v[1] for v in dict_win.values()]))