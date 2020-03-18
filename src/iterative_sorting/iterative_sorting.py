# TO-DO: Complete the selection_sort() function below
test = [5, 10, 3, 6, 13, 2, 4]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for x in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[x]:

                smallest_index = x

        # TO-DO: swap

        if smallest_index != i:

            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


selection_sort(test)
print(test)


# TO-DO:  implement the Bubble Sort function below
test2 = [1, 10, 3, 6, 13, 5, 2, 4]


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for x in range(i):
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
                print(arr[x], arr[x + 1])
    return arr


bubble_sort(test2)
print(test2)
# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
