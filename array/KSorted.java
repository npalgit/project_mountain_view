/* 
Given an array arr of length n where each element is at most k places away from its sorted position,
Plan and code an efficient algorithm to sort arr.
Analyze the runtime and space complexity of your solution.
Sorting order goes from high to low.

Example: n=10, k=2. The element belonging to index 6 in the sorted array, may be at indices 4, 5, 6, 7 or 8 on the given array.
int[] arr= { 4  3  6  5  0  1  2}
int[] result =  {6  5  4  3  2  1  0}
source: http://www.geeksforgeeks.org/nearly-sorted-algorithm/
*/

package interview.array;
import interview.dataStructure.MaxHeap;

class KSorted {
    public static void main(String[] args) {

        System.out.println("test1:");
        int[] arr =  {4, 3, 6, 5, 0, 1, 2};
        int[] result = kSorted(arr, 2);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(result[i] + ", ");
        }

         System.out.println("\ntest2:");
         result = kSorted(arr, 4);
          for (int i = 0; i < arr.length; i++) {
            System.out.print(result[i] + ", ");
        }

        System.out.println("\ntest3:");
         result = kSorted(arr, 10);
          for (int i = 0; i < arr.length; i++) {
            System.out.print(result[i] + ", ");
        }

    }

    public static int[] kSorted(int[] arr, int k) {

        int hSize = k + 1;
        if (hSize > arr.length) {
            hSize = arr.length;
        }

        MaxHeap h = new MaxHeap(hSize);

        for (int i = 0; i < hSize; i++) {
            h.add(arr[i]);
        }

        for(int i = 0; i < arr.length; i++) {
            arr[i] = h.remove();

            if (i + hSize < arr.length)
                h.add(arr[i+hSize]);
        }

        return arr;
    }
} 

