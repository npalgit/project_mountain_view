/* 
  Remove duplicates from an array
  e.g. arr = {3, 3, 1, 2, 3, 4, 5, 5, 6}
  If we don't use hash to implement the method, we will have to sort it.
*/
import java.util.HashSet;  
import java.util.Arrays;
class RemoveDuplicates {
    public static void main(String[] args) {
    
        int[] arr = {1, 2, 3, 3, 3, 4, 5, 5, 6};

        int[] result = removeDuplicatesHash(arr);
        System.out.println("Remove duplicates with hashing");
        System.out.println(Arrays.toString(result));

        System.out.println("Remove duplicates with no hashing");
        result = removeDuplicates(arr);
        System.out.println(Arrays.toString(result));

        System.out.println();
        int[] arr2 = {1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 7};
        //int[] arr2 = {1, 1, 1, 1};
        result = removeDuplicatesHash(arr2);
        System.out.println("Remove duplicates with hashing");
        System.out.println(Arrays.toString(result));

        System.out.println("Remove duplicates with no hashing");
        result = removeDuplicates(arr2);
        System.out.println(Arrays.toString(result));

        System.out.println("Unsorted remove duplicates with hashing");
        int[] arr3 = {9, 1, 5, 1, 7, 1, 2, 5, 3, 4, 3,  9, 5, 5, 7};
        result = removeDuplicatesHash(arr3);
        System.out.println(Arrays.toString(result));

    }


    public static int[] removeDuplicates(int[] arr) {
        if (arr.length == 0 || arr.length == 1)
            return arr;

        int i = 1;
        for (int j = 1; j < arr.length; j++) {
            if (arr[j] != arr[j-1]) {
                if (i != j) // optional
                    arr[i] = arr[j];

                i++;
            }
        }

        if (i < arr.length) arr[i] = '\0';

        return arr;
    }


    /** Using hashset to determine if we can find dupliates. */
    public static int[] removeDuplicatesHash(int[] arr) {

        HashSet<Integer> hs = new HashSet<Integer>();
        if (arr.length == 0 || arr.length == 1)
            return arr;

        int i = 0;
        for (int j = 0; j < arr.length; j++) {

            if (!hs.contains(arr[j])) {
                if (i != j)
                    arr[i] = arr[j];
                i++;
                hs.add(arr[j]);
            }
        }

        if (i < arr.length)
            arr[i] = '\0';

        return arr;
    }


}