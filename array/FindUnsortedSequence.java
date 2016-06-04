/* Given an array of integers, write a method to find indices m and n such that if you sorted 
 * elements m through n, the entire array would be sorted. Minimize n-m, that is, find the smallest 
 * such sequence. 
 * In other words find the subsection of the array, where if this subsection were sorted, the entire array
 * would also be sorted. And we want to minimize the indices of the subsection.
 * Example: 
           0  1  2  3   4   5  6   7  8  9  10  11  12
 * Input:  1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
 * Output: (3, 9) 
 *
 *  1, 2, 4, 7, 10, 17, 7, 12, 6, 7, 16, 18, 19
 * Question source: Cracking the Coding Interview, 5th Edition. Pg 164
 */


class FindUnsortedSequence {

    public static void main(String[] args) {
        int[] arr = new int[]{1, 2, 4, 7, 10, 17, 7, 12, 6, 7, 14, 18, 19};
        findUnsortedSequence(arr);

        arr = new int[]{0, 1,  2, 3, 4, 5, 6, 7, 8};
        findUnsortedSequence(arr);

        arr = new int[]{1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19};
        findUnsortedSequence(arr);

    }

    /** Find the optimal indexes of the unsorted subsequence, sorting which will result in the 
      * entire array being sorted.  */
    public static void findUnsortedSequence(int[] arr) {
        int leftIdx = findLeftIdx(arr);
        int rightIdx = findRightIdx(arr);

        if (leftIdx == -1 || rightIdx == -1) 
            return;

        int[] minMax = findMinMax(arr, leftIdx, rightIdx);
        int min = minMax[0];
        int max = minMax[1];

        leftIdx = extendLeft(arr, min, leftIdx);
        rightIdx = extendRight(arr, max, rightIdx);

        System.out.printf("[%d, %d]\n", leftIdx, rightIdx);
        

    }

    /** Find the min and max value in the subarray.
      * return int[2], int[0] = min, int[1] = max. */
    public static int[] findMinMax(int[] arr, int beg, int end) {
        if (beg > end || beg < 0 || end >= arr.length)
            return new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE};

        int min = arr[beg];
        int max = arr[beg];

        for (int i = beg+1; i <= end; i++) {
            if (arr[i] < min)
                min = arr[i];

            if (arr[i] > max)
                max = arr[i];
        }

        return new int[]{min, max};
    }


    /** Move index by index to the left until reach an index that breaks the decreasing pattern. */
    public static int findRightIdx(int[] arr) {
        for (int i = arr.length-2; i >= 0; i--) {
            if (arr[i] > arr[i+1])
                return i+1;
        }

        return -1;
    }

    /** Move index by index to the right until reach an index that breaks the increasing pattern. */
    public static int findLeftIdx(int[] arr) {
        for (int i = 1; i < arr.length-1; i++) {
            if (arr[i] < arr[i-1])
                return i-1;
        }

        return -1;
    }

    /** Find the left starting index of the optimal subarray. */
    public static int extendLeft(int[] arr, int min, int leftIdx) {
        for (int i = leftIdx; i >= 0; i--) {
            if (arr[i] <= min)
                return i+1;
        }

        return -1;
    }

    /** Find the right ending index of the optimal subarray. */
    public static int extendRight(int[] arr, int max, int rightIdx) {
        for (int i = rightIdx; i < arr.length; i++) {
            if (arr[i] >= max)
                return i-1;
        }

        return -1;
    }


}
