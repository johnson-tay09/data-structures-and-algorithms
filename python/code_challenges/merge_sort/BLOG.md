# Merge Sort
Merge Sort is a way to sort items in an array. Merge sort splits an array in half and sorts each half and then it sorts the two halves back together. It is a recursive function.

### Pseudocode:
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
### Explanation:

- Split the array into two lists.<br>
---2,6,3 | 10,1,5<br>
----left | right<br>

-Call mergeSort for the left half.<br>
-----2,3,6 | 10,1,5<br>
------left | right<br>
-Call mergeSort for the right half.<br>
-----2,3,6 | 1,5,10<br>
------left | right<br>
  
- Merge the left and right together.<br>
-----2,3,6 | 1,5,10<br>
-->1,2
-------3,6 | 5,10<br>
-->1,2,3,5
---------6 | 10<br>
-->1,2,3,5,6,10

- And so on until the array is sorted.<br>
  
### Efficiency:
Time = O(n*logn)<br>
- It will take n time where n is the length of the array times the height of the tree from splitting which is logn.
Space = O(n)<br>
- No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).