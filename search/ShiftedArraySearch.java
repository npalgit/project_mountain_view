/* 
If the sorted array arr is shifted left by an unknown offset and you don't have a pre-shifted copy of it, how would you modify your method to find a number in the shifted array?
shiftArr = [9, 12, 17, 2, 4, 5]

The preshifted version would be:
preShiftArr = [2, 4, 5, 9, 12, 17] 

if num doesn't exist in the array, return -1
*/
class ShiftedArraySearch {

    public static void main(String[] args) {
        System.out.println("Tests for findShiftIdx");

        System.out.print("Shifted Idx is: ");
        int[] arr = {9, 12, 17, 2, 4, 5};
        System.out.println(findShiftIdx(arr, 0, arr.length));

        System.out.print("Shifted Idx is: ");
        int[] arr2 = {12, 12, 12, 13, 1};
        System.out.println(findShiftIdx(arr2, 0, arr2.length));

        System.out.print("Shifted Idx is: ");
        int[] arr3 = {17, 2, 4, 5, 9, 12};
        System.out.println(findShiftIdx(arr3, 0, arr3.length));

        System.out.println("Tests for shiftedArraySearch");

        int key = 2;
        System.out.println("Key is: " + key + ", idx is: " + shiftedArraySearch(arr, 0, arr.length, key));

        key = 9;
        System.out.println("Key is: " + key + ", idx is: " + shiftedArraySearch(arr, 0, arr.length, key));

        key = 12;
        System.out.println("Key is: " + key + ", idx is: " + shiftedArraySearch(arr2, 0, arr2.length, key));

        key = 1;
        System.out.println("Key is: " + key + ", idx is: " + shiftedArraySearch(arr2, 0, arr2.length, key));

        key = 11;
        System.out.println("Key is: " + key + ", idx is: " + shiftedArraySearch(arr3, 0, arr3.length, key));

    }

    public static int shiftedArraySearch(int[] arr, int beg, int end, int key) {
        int shiftedIdx = findShiftIdx(arr, beg, end);

        // Break array in half and do binary Search on each side

        if (arr[0] <= key && key <= arr[shiftedIdx-1]) {
            return binSearch(arr, 0, shiftedIdx-1, key);
        }

        if (arr[shiftedIdx] <= key && key <= arr[arr.length-1]) {
            return binSearch(arr, shiftedIdx, arr.length-1, key);
        }

        return -1;

    }

    /** Regular binardy search. */
    public static int binSearch(int[] arr, int beg, int end, int key) {
        if (beg > end)
            return -1;

        // to prevent overflow: equals (beg + end)/2
        int mid = beg + (end-beg)/2;

        if (key == arr[mid])
            return mid;

        if (key > arr[mid])
            return binSearch(arr, mid+1, end, key);

        return binSearch(arr, beg, mid-1, key);
    }

    /** Modified binary search to find the shifted index. */
    public static int findShiftIdx(int[] arr, int beg, int end) {
        if (beg > end)
            return -1;
        
        int mid = beg + (end-beg)/2;

        if (arr[mid-1] > arr[mid])
            return mid;

        if (arr[mid] >= arr[beg])
            return findShiftIdx(arr, mid, end);

        return findShiftIdx(arr, beg, mid);
    }
}
