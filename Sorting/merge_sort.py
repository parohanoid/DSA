# Strategy:

# if one number quit
# Sort the left half
# Sort the right half
# Merge the two halves [magic]
# if the two halves are only one element, MERGE BY keep the first half on the left, second half on the right

in_list = [6,3,4,1,5,2,7,0]

# two functions, merge_sort and merge
# merge_sort - 
# if one element, then returns the array
# takes two arrays and applies merge_sort to the left and right halves and stores them into sorted left and sorted right
# at the end, applies merge(left_sorted, right_sorted) and returns it (this is the magic step when two sorted arrays are merged. Two arrays are sorted because this step is only reached/first executed when the two arrays are singular or they are sorted by recursion)

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    return merge(left_sorted, right_sorted)

def merge(left, right):
    i = j = 0
    result = []
    # loop through the left and right arrays until any one of them is empty
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    # if any one of them is not empty by the end of the iterations, extend it to result, first left and then right
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort(in_list))

# visualise this at https://pythontutor.com/python-compiler.html#mode=edit