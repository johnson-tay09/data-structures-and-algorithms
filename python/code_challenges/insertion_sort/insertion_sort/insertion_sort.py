def insertion_sort(arr):
    # for each char in the array
    if len(arr) < 1:
        return "Not a valid input"
    if len(arr) == 1:
        return arr
    for char in range(1, len(arr)):
        # set check_char to 0
        check_char = char - 1
        # set temp to arr at 1
        temp = arr[char]
        # iterate through the array and check if temp is < arr[check]
        while check_char >= 0 and temp < arr[check_char]:
            # move a the check_char +1 to the check_char position
            arr[check_char + 1] = arr[check_char]
            # set check_char to check_char minus 1
            check_char = check_char - 1
        # set temp to the position after check_char
        arr[check_char + 1] = temp
    return arr
