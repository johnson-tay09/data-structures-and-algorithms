# Insertion Sort
Insertion sort is a way to sort an array of values in python. It goes through the array and compares two values and moves the smaller one closer to the 0 index. 

### Pseudocode:
SelectionSort(int[] arr)
    DECLARE n <-- arr.Length;
    FOR i = 0; i to n - 1  
        DECLARE min <-- i;
        FOR j = i + 1 to n
            if (arr[j] < arr[min])
                min <-- j;

        DECLARE temp <-- arr[min];
        arr[min] <-- arr[i];
        arr[i] <-- temp;
### Explanation:

- Split the array into a sorted and unsorted sub-list. Sorted sub list starts with a length of 1.<br>
-------4 | 2,6,3,10,1<br>
--sorted | unsorted<br>

- Move the first item from unsorted to sorted and compare the value to the immediate left.<br>
-----4,2 | 6,3,10,1<br>
  
- If the left is higher they change positions until the left value is no longer higher and then the item is properly sorted.<br>
-----2,4 | 6,3,10,1<br>
---2,4,6 | 3,10,1<br>
-2,4,6,3 | 10,1 --> <br>
-2,4,3,6 | 10,1 --> <br>
-2,3,4,6 | 10,1  <br>
- And so on until the array is sorted.<br>
  
### Efficiency:
Time = O(n)<br>
- It will take n time where n is the length of the array.
Space = O(n)<br>
- No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).