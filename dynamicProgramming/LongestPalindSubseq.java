import java.util.*;

/* Given a sequence, find the length of the longest palindromic subsequence in it. 
 * For example, if the given sequence is “BBABCBCAB”, then the output should be 7 as “BABCBAB”
 * is the longest palindromic subseuqnce in it. “BBBBB” and “BBCBB” are also palindromic subsequences
 * of the given sequence, but not the longest ones. */

class LongestPalindSubseq {
    public static void main(String args[]) {
        char[] arr = {'B', 'B', 'A', 'B', 'C', 'B', 'C', 'A', 'B'};

        // Brute force method length
        int ans = lps_brute(arr, 0, arr.length-1);
        System.out.println("Brute force: " + ans);

        // Brute force method sequence
        ArrayDeque<Character> chars = lps_brute_sequence(arr, 0, arr.length-1);
        System.out.print("Bruce force sequence: ");
        for (Character c : chars) {
            System.out.print(c + ", ");
        }
        System.out.println();
    }

    /** Longest Palindrome Subsequence using top-down brute force recursion. */
    public static int lps_brute(char[] arr, int beg, int end) {
        if (beg > end)
            return 0;

        int curr_len = 0;
        int result = 0;
        if (arr[beg] == arr[end]) {
            if (beg == end)
                curr_len = 1;
            else
                curr_len = 2;

            result = lps_brute(arr, beg+1, end-1);

        } else {
            result = lps_brute(arr, beg+1, end);
            int rhs = lps_brute(arr, beg, end-1);
            if (rhs > result)
                result = rhs;
        }
        return result + curr_len;
    }

    /** Longest Palindrome Subsequence using top-down brute force recursion
      * Print out the longest sequence rather than length. */
    public static ArrayDeque<Character> lps_brute_sequence(char[] arr, int beg, int end) {

        if (beg > end)
            return new ArrayDeque<Character>();

        ArrayDeque<Character> curr_queue = new ArrayDeque<Character>();
        ArrayDeque<Character> result = new ArrayDeque<Character>();

        if (arr[beg] == arr[end]) {
            if (beg == end) {
                result.addFirst(arr[beg]);
                return result;
            }
            else {
                curr_queue.addFirst(arr[beg]);
                curr_queue.addLast(arr[end]);
            }

            result = lps_brute_sequence(arr, beg+1, end-1);

        } else {
            result = lps_brute_sequence(arr, beg+1, end);
            ArrayDeque<Character> rhs = lps_brute_sequence(arr, beg, end-1);
            if (rhs.size() > result.size())
                result = rhs;
        }

        if (curr_queue.size() == 0)
            return result;
       
        result.addFirst(curr_queue.pollFirst());
        result.addLast(curr_queue.pollLast());

        return result;
    }

    /** Longest Palindrome Subsequence using dynamic programming. */
    public static ArrayDeque<Character> lps_dp(char[] arr, int beg, int end) {

    }

}
