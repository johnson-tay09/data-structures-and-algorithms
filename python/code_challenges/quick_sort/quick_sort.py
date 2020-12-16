def partition(arr, left, right):
    # index of smaller element
    i = left - 1
    # pivot element
    pivot = arr[right]

    for j in range(left, right):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr, left, right):
    if len(arr) == 0:
        return "Not a valid input"
    if len(arr) == 1:
        return arr
    if left < right:
        partition_index = partition(arr, left, right)

        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)
    return arr


# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quick_sort(arr, 0, n - 1)
# print("Sorted array is:")
# for i in range(n):
#     print("%d" % arr[i]),