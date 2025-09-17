fruits = [3,3,2,1,2,1,0]



# window is jthe state dict
# start is the record of the beginning of the window
# loop through the array and increment the count of the fruits in the window (if doesn't exist assign 0 and increment)
# we always reduce the window till the unique count in windows is <=2 (thats the point of while loop) 

def fruit_into_baskets(fruits):
    max_fruit = 0
    state = {}
    start = 0
    for i, fruit in enumerate(fruits):
        state[fruit] = state.get(fruit, 0) + 1
        while len(state) > 2:
            state[fruits[start]] -= 1
            if (state[fruits[start]] == 0):
                del state[fruits[start]]
            start += 1
        max_fruit = max(max_fruit, i - start + 1)
    return max_fruit

print(fruit_into_baskets(fruits))