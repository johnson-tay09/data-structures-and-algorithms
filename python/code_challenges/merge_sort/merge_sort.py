
def merge_sort(arr):
    n = len(arr)
    # split the array in half
    if n == 1:
        return arr
    if n == 0:
        return "Not a valid input"
    if n > 1:
        mid = n//2
        left = arr[:mid]
        right = arr[mid:]
        # sort the left side
        merge_sort(left)
        # sort the right side
        merge_sort(right)
        # sort them together in the correct order
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr

    
