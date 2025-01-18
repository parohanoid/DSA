# https://leetcode.com/problems/container-with-most-water/description/

# why the small height pointer should be the one to move is: With small height pointer, we already got the max area we could achieve as any wall we may we use with that, it would always be less than that as height would never be more than small height.

def naive_max(list):
    max_area = 0
    i, j = 0, len(heights) - 1
    
    # O(n)
    while i < j:
        width = abs(i - j)
        height = min(list[i], list[j])
        cur_area = width * height
        max_area = max(max_area, cur_area)
        if list[i] < list[j]:
            i += 1
        else:
            j -= 1
    return max_area

    # naive: O(n^2)
    # for i in range(len(list)):
    #     for j in range(i, len(list)):
    #         cur_area = min(list[i], list[j]) * abs(i - j)
    #         if cur_area > max_area:
    #             max_area = cur_area
    # return max_area


heights = [3,4,1,2,2,4,1,3,2]

print(naive_max(heights))