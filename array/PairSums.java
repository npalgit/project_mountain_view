/* Given an array, print all pairs of numbers that sum up to a particular value. There may or may notbe duplicates */
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Arrays;

class PairSums {
    public static void main(String[] args) {

        int[] arr = new int[]{-2, -1, 0, 2, 3, 5, 6, 5, 5, 7, 9, 13, 5, 14, -7};
        System.out.println("test1");
        findPairSumsIndex(arr, 10);   
        System.out.println(); 
        findPairSumsIndexHash(arr, 10);   
        System.out.println(); 
        findPairSumsIndexHash2(arr, 10);   
        System.out.println(); 

        System.out.println("test2");
        findPairSumsIndex(arr, 0);   
        System.out.println();
        findPairSumsIndexHash(arr, 0);   
        System.out.println(); 
        findPairSumsIndexHash2(arr, 0); 

    }

    /** Print out all numbers that sum up to a paritcular value without using hash tables. */
    public static void findPairSumsIndex(int[] arr, int sum) {
        Arrays.sort(arr);
        int beg = 0;
        int end = arr.length-1;

        while (beg <= end) {
            int tempSum = arr[beg] + arr[end];
            if (tempSum == sum) {
                System.out.printf("values: [%d, %d] indices: [%d, %d]\n", arr[beg], arr[end], beg, end);
                beg++;
                end--;
            } else if (tempSum < sum) {
                beg++;
            } else {
                end--;
            }

        }
    }

    /** Print out all numbers that sum up to a particular value. Array could contain duplicates. */
    public static void findPairSumsIndexHash(int[] arr, int sum) {
        HashMap<Integer, LinkedList<Integer>> map = new HashMap<Integer, LinkedList<Integer>>();
        
        for (int i = 0; i < arr.length; i++) {
            int targetComp = sum - arr[i];

            if (map.containsKey(targetComp)) {
                LinkedList<Integer> list = map.get(targetComp);
                Integer targetIdx = list.removeFirst();
                System.out.printf("values: [%d, %d] indices: [%d, %d]\n", targetComp, arr[i], targetIdx, i);

                if (list.isEmpty()) 
                    map.remove(targetComp);
                else
                    map.put(targetComp, list);
            } else {
                LinkedList<Integer> list = new LinkedList<Integer>();
                list.add(i);
                map.put(arr[i], list);
            }
        }

    }

    /** An alternate version of print out all numbers that sum up to a particular value.
      * The detailed implementation of adding to hashmap is different. */
    public static void findPairSumsIndexHash2(int[] arr, int sum) {
        HashMap<Integer, LinkedList<Integer>> map = new HashMap<Integer, LinkedList<Integer>>();
        for (int i = 0; i < arr.length; i++) {

            if (map.containsKey(arr[i])) {
                LinkedList<Integer> list = map.get(arr[i]);
                Integer originalIdx = list.removeFirst();
                System.out.printf("values: [%d, %d] indices: [%d, %d]\n", arr[originalIdx], arr[i], originalIdx, i);

                if (list.isEmpty())
                    map.remove(arr[i]);
                else 
                    map.put(arr[i], list);
            } else {
                int targetComp = sum - arr[i];
                LinkedList<Integer> list = new LinkedList<Integer>();
                list.add(i);
                map.put(targetComp, list);
            }
        }
    }

}
