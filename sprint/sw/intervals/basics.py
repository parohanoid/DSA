# intervals need to be sorted to go through them

# Checking overlaps
def canAttendMeetings(intervals):
    if not intervals:
        return True
    
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    
    return True

# merging overlaps
# return a list after merging all overlaps
def mergeIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    merged = []
        
    for interval in sortedIntervals:
        # the second condition means that the current interval's start time is not greater than or equal to the last interval of the merged list's end time (current interval is not overlapping with the last merged interval)
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(interval[1], merged[-1][1])

    return merged