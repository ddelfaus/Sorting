# from iterative_sorting import selection_sort

# STRETCH: implement Linear Search
#
test = [3, 7, 22, 8, 4, 1]


def linear_search(arr, target):

    # TO-DO: add missing code
    for i in range(len(arr)):
        if arr[i] == target:
            print("target", target)
            print("found", i)
            return i
        else:
            print("target", target)
            print("not found")
    return -1   # not found


linear_search(test, 22)
# STRETCH: write an iterative implementation of Binary Search
# div array by 2
# compare mid value to target
# if same found
# if diff find smaller or larger
# shorten the array base on smaller or larger
test2 = [3, 7, 22, 8, 4, 1]


def binary_search(arr, target):
    arr.sort()
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1
    found = False
    print(high)
    while (low <= high and not found):
        mid = (low + high)//2
        if arr[mid] == target:
            found = True
        else:
            if target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
    # TO-DO: add missing code

    return -1  # not found


binary_search(test2, 1)
# STRETCH: write a recursive implementation of Binary Search


def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
