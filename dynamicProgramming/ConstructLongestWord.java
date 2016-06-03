/* 
 * Given a list of words, write a program to find the longest word made of other words in the list. 
 * Example:
 * Input: cat, banana, dog, nana, walk, walker, dogwalker.
 * Output: dogwalker
 * Question source: Cracking the Coding Interview 5th edition, Pg 471. My own solution. */

import java.util.HashSet;
import java.util.Arrays;

class ConstructLongestWord {

    public static void main(String[] args) {
        String[] strArr = {"cat", "dog", "nana", "walk", "banana", "walker", "dogwalker"};

        String[] strArr2 = {"er", "do", "na", "dog", "dogw", "walk", "ernana",  "walker", "dogwalkernana"};

        String[] strArr3 = {"er", "do", "dog", "dogw", "walk",  "walker", "dogwalkernana"};

        // Assume we can sort strARr by length. The list above is already sorted by length
        HashSet<String> dict = new HashSet<String>();

        System.out.println(findLongestWord(strArr));

        System.out.println(findLongestWord(strArr2));

        System.out.println(findLongestWord(strArr3));

    }

    /** Find the longest word made of other words in the list. */
    public static String findLongestWord(String[] strArr) {
        HashSet<String> dict = new HashSet<String>();

        for (String str : strArr) {
            dict.add(str);
        }

        for (int i = strArr.length-1; i >= 0; i--) {
            if (canConstructWord(dict, strArr[i]))
                return strArr[i];
        }

        return null;
    }

    /** Given a word find out if this word can be constructed using the dict given. */
    public static boolean canConstructWord(HashSet<String> dict, String word) {
        if (dict.contains(word))
            dict.remove(word);

        boolean partial[] = new boolean[word.length()+1];
        partial[word.length()] = true;

        for (int i = word.length()-1; i >= 0; i--) {
            for (int j = i; j < word.length(); j++) {
                if (dict.contains(word.substring(i, j+1)) && partial[j+1]) {
                    partial[i] = true;
                    break;
                }
            }
        }
        return partial[0];
    }

}