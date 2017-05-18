import java.io.*;
import java.util.*;
/*
 All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#187
*/
class RepeatSeq {
    public static void main(String args[]) {
        String s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
        List<String> rslt = repeatSeq(s);
        for (String r : rslt) {
            System.out.println(r);
        }
    }

    public static List<String> repeatSeq(String s) {
        List<String> res = new ArrayList<String>();
        if (s.length() < 11) return res;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        
        map.put('A', 0);
        map.put('C', 1);
        map.put('G', 2);
        map.put('T', 3);
        
        // 0011 1111 1111 1111 1111 
        int mask = 0x3ffff;
        HashSet<Integer> seen = new HashSet<Integer>();
        HashSet<Integer> repeat = new HashSet<Integer>();

        // init
        int code = 0;
        for (int i = 0; i < 9; i ++) {
            code = (code & mask) << 2 | map.get(s.charAt(i));
        }

        for (int i = 9; i < s.length(); i ++) {
            code = (code & mask) << 2 | map.get(s.charAt(i));
            if (!seen.add(code) && repeat.add(code)) {
                res.add(s.substring(i - 9, i + 1));
            }
        }
        return res;
        
    }
}
