# height = [5,4,1,2]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
out = 10

# decrease and then increase
# min of decrease and increase
# width between decrease and increase

area = 0

i = 0
while (i < len(height)-2):
    if height[i] > 0:
        end = i + 1
        for j in range(i+1, len(height)):
            if (height[j] >= height[i]) or ((j == len(height)-1 and (height[j] > height[j-1])) ):
                end = j
                max_height = min(height[j], height[i])
                break
        i = height.index(min(filter(lambda x: x > height[end], height[i:end])))
        for k in range(i+1, end):
            area += max_height - height[k]
        i = end
    else:
        i += 1

print(area)