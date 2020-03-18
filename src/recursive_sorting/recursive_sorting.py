# TO-DO: complete the help function below to merge 2 sorted arrays

#------------------
#think of way to solve it with the smallest problem


# Merge sort
# 1, 5, 6, 2, 10, 3, 9, 4,
# # divide in half until you have arrays of 1
# 1,    5,     6,     2,    10,     3,   9,    4,

# # merge 2 arrays together in order
# 1,5   2,6   3,10   4,9
# # merge 2 arrays look at the front of each subarray and empty arrays are just filled in 
# 1,2,5,6         3,4,9,10

# 1,2,3,4,5,6,9,10
# def split(arr, size):
#     arrs = []
#     while len(arr) > size:
#         pice = arr[:size]
#         arrs.append(pice)
#         arr = arr [1:]
#     arrs.append(arr)
#     return arrs


# test1 = [ 1, 5, 6, 2, 10, 3, 9, 4,]
# print(split(test1,1))


def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # given two arrays
    #combine into a sorted array
    #do this by ....
    #compare the first element of each
    #add the smallest to the merged array
    #iterate the pointer for the smaller value
    #if one pointer reachers the end of it's array
    # push all remaining values in the other array to end of merged


    
    left = 0
    right = 0

    for i in range(0 , elements):
        if left < len(arrA) and  right < len(arrB):
            if (arrA[left] < arrB[right]):
                merged_arr[i] = arrA[left]
                left += 1
            else:
                merged_arr[i] = arrB[right]
                right += 1
        elif left < len(arrA):
            merged_arr[i] = arrA[left]
            left += 1
        elif right < len(arrB):
            merged_arr[i] = arrB[right]
            right += 1






    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #Base case: arr length 0 or 1


    # Otherwise:
    #find middle of array with //2
    # divide to left and right
    # do merge sort on left and right
    # put it back together by merging left and right

    pivot = int(len(arr)/2) #This is the pivot
    if len(arr) > 1:
        # recursively call merge_sort() on LHS
        left = merge_sort(arr[:pivot])
        # recursively call merge_sort() on RHS
        right = merge_sort(arr[pivot:])
        # merge sorted pieces
        arr = merge(left, right)

    return arr

print(merge_sort([0, 1, 4, 7, 2, 10]))

# print(merge_sort(test1))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
