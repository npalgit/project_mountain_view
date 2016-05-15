package interview.dataStructure;
import java.util.Arrays;
/** Heap implementation based on:
        https://www.cs.auckland.ac.nz/software/AlgAnim/heaps.html */
public class MaxHeap {

    private static final int FRONT = 1;

    //ArrayList to hold the heap
    private int[] heapArr;

    // Points to the empty array cell that can push data onto
    private int ptr = 0;
    
    private int getLeftChildIdx(int i) {
        return 2*i;
    }

    private int getRightChildIdx(int i) {
        return 2*i + 1;
    }

    private int getParentIdx(int i) {
        return i/2;
    }

    private void swap(int idx1, int idx2) {
        int temp;
        temp = heapArr[idx1];
        heapArr[idx1] = heapArr[idx2];
        heapArr[idx2] = temp;
    }

    //Constructs the heap - heapify
    public MaxHeap(int size) {
        // heap starts at index 1
        heapArr = new int[size+1];
        Arrays.fill(heapArr, Integer.MIN_VALUE);
    }

    public void add(int key) {
        if (ptr + 1 < heapArr.length) {
            ptr++;
            heapArr[ptr] = key;
        } else {
            return ;
        }

        int i = ptr;

        int parent = getParentIdx(i);

        while (heapArr[parent] < heapArr[i] && parent > 0) {
            swap(parent, i);
            i = parent;
            parent = getParentIdx(i);
        }
    }

    public int peek()
    {
        return heapArr[FRONT];
    }

    public void percolateUp(int key) {
        if (ptr < 1)
            return ;

        heapArr[FRONT] = key;

        int i = FRONT;
        int leftChildIdx; 
        int rightChildIdx;
        int leftChild;
        int rightChild; 

        while(i <= ptr/2) {

            leftChildIdx = getLeftChildIdx(i);
            rightChildIdx = getRightChildIdx(i);
            leftChild = heapArr[leftChildIdx];
            rightChild = heapArr[rightChildIdx];
          
            if (leftChild >= rightChild && leftChild > heapArr[i]) {
                swap(leftChildIdx, i);
                i = leftChildIdx;
            } 
            else if (rightChild > leftChild && rightChild > heapArr[i]) {
                swap(rightChildIdx, i);
                i = rightChildIdx;
            } else {
                return;
            }
        } 

        
    }

    public int remove() {
        int head = heapArr[FRONT];

        int lastElement = heapArr[ptr];
        heapArr[ptr] = Integer.MIN_VALUE;
        ptr--;

        percolateUp(lastElement);

        return head;
    }

    public int size() {
        return ptr;
    }

    public boolean isEmpty()
    {
        if (ptr < 1)
            return true;

        return false;
    }

    public void print()
    {
        for (int i = 1; i <= ptr/ 2 ; i++ )
        {
            System.out.print(" PARENT : " + heapArr[i] + " LEFT CHILD : " + heapArr[getLeftChildIdx(i)]
                  + " RIGHT CHILD :" + heapArr[getRightChildIdx(i)]);
            System.out.println();
        }
    }
    

    public static void main(String[] args) {

        System.out.println("The Max Heap is ");
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

        System.out.println("The Max Heap is ");
        maxHeap.add(70);
        maxHeap.print();
        System.out.println("The max val is " + maxHeap.remove());
        maxHeap.print();
    

    }
}