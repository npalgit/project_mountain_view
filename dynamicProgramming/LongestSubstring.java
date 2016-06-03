/* Given two strings str1 and str2, find the length of longest common substring between them.
 * e.g. str1 = "AGGTABX", str2 = "GTABXGT", longest common substring = "GTABX" len = 5 */
import java.util.Arrays;

class LongestSubstring {
    public static void main(String[] args) {
        String str1 = "helloworld";
        String str2 = "ehllohelloworld";

        int[] result = ls_recursion(str1, str2, 0, 0);
        System.out.println(Arrays.toString(result));
        System.out.println(ls_dp(str1, str2));

        str1 = "AGGTABX"; 
        str2 = "GTABXGT";
        result = ls_recursion(str1, str2, 0, 0);
        System.out.println(Arrays.toString(result));
        System.out.println(ls_dp(str1, str2));

    }

    /** Find the longest substring using top-down, brute force, recursion.
      * Return type: int[], int[0] = longest_overall, int[1] = current_path_len. */
    public static int[] ls_recursion(String str1, String str2, int i, int j) {
        if (i >= str1.length() || j >= str2.length())
            return new int[2];

        int longest_overall = 0;
        int current_path_len = 0;

        if (str1.charAt(i) == str2.charAt(j))
            current_path_len = ls_recursion(str1, str2, i+1, j+1)[1] + 1;

        int lhs = ls_recursion(str1, str2, i+1, j)[0];
        int rhs = ls_recursion(str1, str2, i, j+1)[0];

        longest_overall = (lhs > rhs)? lhs : rhs;

        if (current_path_len > longest_overall) 
            longest_overall = current_path_len; 

        return new int[]{longest_overall, current_path_len};
    }

     /** Find the longest substring using dynamic programming. */
    public static int ls_dp(String str1, String str2) {
        int max_len = 0;

        // opt[0][j], opt[i][0] are all zeros, base case, makes loops simpler.
        int[][] opt = new int[str1.length()+1][str2.length()+1];

        for (int i = 1; i <= str1.length(); i++) {
            for (int j = 1; j <= str2.length(); j++) {
                if (str1.charAt(i-1) == str2.charAt(j-1)) {
                    opt[i][j] = opt[i-1][j-1] + 1;

                    if (opt[i][j] > max_len)
                        max_len = opt[i][j];
                }
            }
        }

        return max_len;
    }
}
