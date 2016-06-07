/* Find the first non-repeating character in a string. */
import java.util.*;

class FirstNonRepeatingElement {

    public static void main(String[] args) {
        String str = "GeeksForGeeks";
        char c = firstNonRepeating(str.toCharArray());
        System.out.println(c);

        str = "GeeksQuiz";
        c = firstNonRepeating(str.toCharArray());
        System.out.println(c);

        str = "eeeee";
        c = firstNonRepeating(str.toCharArray());
        System.out.println(c);

        str = "GeeksForGeeks";
        c = firstNonRepeatingEfficient(str.toCharArray());
        System.out.println(c);

        str = "GeeksQuiz";
        c = firstNonRepeatingEfficient(str.toCharArray());
        System.out.println(c);

        str = "eeeee";
        c = firstNonRepeatingEfficient(str.toCharArray());
        System.out.println(c);
    }

    /** Find first non-repeating character, less efficient. */
    public static char firstNonRepeating(char[] arr) {
        char[] count = new char[256];

        for (int i = 0; i < arr.length; i++) {
            char c = arr[i];
            count[c]++;
        }

        for (int i = 0; i < arr.length; i++) {
            char c = arr[i];
            if (count[c] == 1)
                return c;
        }

        return '\0';

    }

    /** Find first non-repeating character, more efficient, slightly different implementation on how the 
      * the character is returned. */
    public static char firstNonRepeatingEfficient(char[] arr) {
        char[] count = new char[256];
        int[] firstIdx = new int[256];
        Arrays.fill(firstIdx, -1);

        for (int i = 0; i < arr.length; i++) {
            char c = arr[i];
            count[c]++;

            if (firstIdx[c] == -1) {
                firstIdx[c] = i;
            }
        }

        // extract the first index
        int minIdx = Integer.MAX_VALUE;

        for (int i = 0; i < count.length; i++) {
            if (count[i] == 1 && firstIdx[i] <= minIdx) {
                minIdx = firstIdx[i];
            }
        }

        if (minIdx == Integer.MAX_VALUE)
            return '\0';
        
        return arr[minIdx];

    }


}
