def nonOverlappingIntervals(intervals):
    if not intervals:
        return 0

    # sorting by the endings always sorts automatically by the smallest interval in the beggining because the start point will always be less than the end point for an interval
    # so the first interval will be the smallest one and will always be non Overlapping with the others
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 1

    for i in range(1, len(intervals)):
        # Non-overlapping interval found
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1

    return len(intervals) - count # returns the overlapping interval count

intervals = [[4,6],[11, 17],[7,10],[2,18]]
# print(nonOverlappingIntervals(intervals))

# DESCRIPTION (credit Leetcode.com)
# Write a function to check if a person can attend all the meetings scheduled without any time conflicts. Given an array intervals, where each element [s1, e1] represents a meeting starting at time s1 and ending at time e1, determine if there are any overlapping meetings. If there is no overlap between any meetings, return true; otherwise, return false.

# Note that meetings ending and starting at the same time, such as (0,5) and (5,10), do not conflict.

# Input:

# intervals = [(1,5),(3,9),(6,8)]
# Output:

# def mergeSort(arr):

#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]
#     left_sorted = mergeSort(left)
#     right_sorted = mergeSort(right)
    
#     def merge(left, right):
#         l = 0
#         r = 0

#         while l < 
        


# false
intervals = [(1,5),(3,9),(6,8)]
# def nonOverlapping(arr):
    


print(nonOverlappingIntervals(intervals))