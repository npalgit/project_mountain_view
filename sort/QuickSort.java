import java.util.Arrays;

/*  Algorithm based on CLRS textbook. */
class QuickSort {
    public static void main(String[] args) {
        int[] arr = {5, 6, 8, 1, 9, 4, 3};

        quickSort(arr, 0, arr.length-1);
        System.out.println(Arrays.toString(arr));

        int[] arr2 = {9, 5, 4, 3, 2, 1, 0};
        quickSort(arr2, 0, arr2.length-1);
        System.out.println(Arrays.toString(arr2));


    }

    public static void quickSort(int[] arr, int beg, int end) {
        if (beg <= end) {
            int pivotIdx = partition(arr, beg, end);
            quickSort(arr, beg, pivotIdx-1);
            quickSort(arr, pivotIdx+1, end);
        }

    }

    public static int partition(int[] arr, int beg, int end) {
        int pivot = arr[end];

        int i = beg-1;

        for (int j = beg; j <= end; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
               
            }

        }

        return i;
    }
}
