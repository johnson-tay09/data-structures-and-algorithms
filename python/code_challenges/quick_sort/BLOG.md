# Quick Sort
Quick sort is a way to sort items in a list. Pivot is defined having all items to the left be smaller and to the right be larger. 

### Pseudocode:
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
### Explanation:

- Select a pivot. For example we will select "5".<br>
---2,6,3,10,1,**5**<br>

-Next we compare the value of each remaining index value to the pivot. Lower values go to the left list and larger ones go to the right list. Next we put the pivot where it belongs and then repeat the process with a new pivot.<br>
-----2,3,1 | 10,6<br>
------left | right<br>
---> 2,3,1,5,10,6<br>
--->Repeat until list is sorted.

### Efficiency:
Time = O(n^2)<br>
- It will take n^2 time because each object has to be compared for each pivot selected.
Space = Olog(n)<br>