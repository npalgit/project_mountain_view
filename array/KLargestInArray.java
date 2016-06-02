/*
 Given an array and a number k where k is smaller than size of array,
 we need to find the k’th largest element in the given array. 
 It is given that all array elements are distinct

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 4
Output: 4

Question adapted from: http://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
*/
package interview.array;
import interview.dataStructure.MaxHeap;

class KLargestInArray {
    public static void main(String[] args) {
        int[] arr = {7, 10, 4, 3, 20, 15};
        int k;
        k = 3;
        System.out.println("k = " + k + ": " + findKthLargest1(arr, k));

        k = 4;
        System.out.println("k = " + k + ": " + findKthLargest1(arr, k));

    } 

    /** Find the kth largest by heapifying the whole thing */
   public static int findKthLargest1(int[] arr, int k) {
        MaxHeap maxHeap = new MaxHeap(arr.length);

        for (int i = 0; i < arr.length; i++) {
            maxHeap.add(arr[i]);
        }

        for (int i = 0; i < k; i++)
        {
            maxHeap.remove();
        }

        return maxHeap.remove();
    }
}



