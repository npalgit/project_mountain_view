import java.io.*;
import java.util.*;

/*
 * Given a list of words of equal length, and a dictionary, write a method to transform one word into naother word by
 * changing only one letter at a time. The new word you get in each step must be in the dictionary.
 * e.g.
 * dict1= 'aaa\n abb\n bbb\n aba\n acc\n abc\n ccc \n aad'
 * output: ['aaa', 'aba', 'abc']
 */
public class WordLadder {
  public static void main(String[] args) {

    System.out.println("test1");
    ArrayList<String> wordList = new ArrayList<String>();
    wordList.add("hot");
    wordList.add("hik");
    wordList.add("dot");
    wordList.add("dog");
    wordList.add("lot");
    wordList.add("log");
    wordList.add("cog");

    String beg = "hit";
    String end = "cog";

    int result = wordLadder(beg, end, wordList);
    System.out.println(result);

  }

  public static int wordLadder(String beg, String end, List<String> wordList) { 
    if (wordList == null || beg == null || end == null)
      return 0;

    HashSet<String> wSet = new HashSet<String>(wordList);
    System.out.println(wSet.toString());
    LinkedList<Itm> q = new LinkedList<Itm>();
    q.add(new Itm(beg, 1));
    while (!q.isEmpty()) {
        Itm itm = q.remove();
        Iterator<String> itr = wSet.iterator();
        while (itr.hasNext()) {
            String itr_w = itr.next();
            if (compareStrings(itr_w, itm.word)) {
                if (itr_w.equals(end))
                    return itm.level + 1;
                q.add(new Itm(itr_w, itm.level+1));
                itr.remove();
            }
        }

    }

    return 0;
  }
 
  public static boolean compareStrings(String str1, String str2) {
    int count = 0;
    
    // if only one character differs return true.
    for (int i = 0; i< str1.length(); i++) {
      if (str1.charAt(i) != str2.charAt(i))
        count++;
      
      if (count > 1)
        return false;
    }
    
    if (count == 0)
      return false;
    
    return true;  
  }
}

class Itm {
    public String word;
    public int level;

    public Itm(String word, int level) {
        this.word = word;
        this.level = level;
    }
}
