/* Given a string s and an array of smaller strings T, design a method to search s for each small string in T.
 * Question source: Cracking the Coding Interview 5th Edition. Pg 168.
 * Solution source: my own 
 */
package interview.string;
import interview.dataStructure.SuffixTree;

class SearchForSubstring {
    public static void main(String[] args) {

        System.out.println(searchForSubstringSuffixTree("abaaba", "hello"));
        System.out.println(searchForSubstringSuffixTree("abaaba", "ab"));
        System.out.println(searchForSubstringSuffixTree("abaaba", "aa"));
        System.out.println(searchForSubstringSuffixTree("abaaba", "a"));
        System.out.println(searchForSubstringSuffixTree("abaaba", "aaba"));
        System.out.println();
       
        System.out.println(searchForSubstringSuffixTree("helloworld", "hello"));
        System.out.println(searchForSubstringSuffixTree("helloworld", "owo"));
        System.out.println(searchForSubstringSuffixTree("helloworld", "rld"));
        System.out.println(searchForSubstringSuffixTree("helloworld", "dl"));
        System.out.println(searchForSubstringSuffixTree("helloworld", "l"));
        System.out.println(searchForSubstringSuffixTree("helloworld", "owor"));
        System.out.println(searchForSubstringSuffixTree("helloworld", "lwo"));

    }

    /** Search for the substring using suffix tree.
      * NOTE: This problem is then primarily about implementation of the suffix tree. 
      *        I created my own suffix tree. */
    public static boolean searchForSubstringSuffixTree(String str, String substr) {
        SuffixTree stree = new SuffixTree(str);
        return stree.containsSubstring(substr);
    }


}
