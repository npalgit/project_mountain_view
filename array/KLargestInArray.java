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



//sorted: {20, 15, 10, 7, 4, 3, 0, 20, 30, 50}
{20, 15, 10, 7, 4, 3, 20, 21, 30, 50}
                                  -

 0  1  2  3    4   5   6    7   8   9                               -
{3, 4, 7, 10, 15, 20, 20,  21, 30, 50} 
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

       /* System.out.println("The Max Heap is ");
        MaxHeap maxHeap = new MaxHeap(10);
        maxHeap.add(5);
        maxHeap.add(3);
        maxHeap.add(17);
        maxHeap.add(10);
        maxHeap.add(84);
        maxHeap.add(19);
        maxHeap.add(6);
        maxHeap.add(22);
        maxHeap.add(9);
 
        maxHeap.print();
        System.out.println("The max val is " + maxHeap.remove());
        maxHeap.print();

        System.out.println("The max val is " + maxHeap.remove());
        maxHeap.print();

        System.out.println();
        maxHeap.add(70);
        maxHeap.print();
        System.out.println("The max val is " + maxHeap.remove());
        maxHeap.print(); */


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


    /** Find the kth largest by heapifying the first k heap */
   /*public static int findKthLargest2(int[] arr, int k) {

        int[] arrHeap = new int[k+1];

        MaxHeap maxHeap = new MaxHeap(arrHeap);

        for (int i = 0; i <= arr.length; i++)
        {
            maxHeap.add(arr[i]);
        }

        for (int i = 0; i < k; i++) {
            System.out.println(maxHeap.remove());
        }
        return maxHeap.remove();
    }*/


}


// minHeap() => size k

// k + (n-k)log(k)
// k + nlog(k)

// n + klog(n)

