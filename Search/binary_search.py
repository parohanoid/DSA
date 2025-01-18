# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/workspaces/DSA/Sorting')

from merge_sort import *

def bin_search(arr, x):
    low = 0
    high = len(arr)
    
    while low <= high:    
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1    
    return -1



in_list = [10, 2, 3, 4, 40]
print(bin_search(merge_sort(in_list), 10))