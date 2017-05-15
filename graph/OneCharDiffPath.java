import java.io.*;
import java.util.*;

/*
 * Given a list of words of equal length, and a dictionary, write a method to transform one word into naother word by
 * changing only one letter at a time. The new word you get in each step must be in the dictionary.
 * e.g.
 * dict1= 'aaa\n abb\n bbb\n aba\n acc\n abc\n ccc \n aad'
 * output: ['aaa', 'aba', 'abc']
 */
public class OneCharDiffPath {
  public static void main(String[] args) {

    ArrayList<String> dict = new ArrayList<String>();

    System.out.println("test1");
    dict.add("aaa");
    dict.add("abb");
    dict.add("bbb");
    dict.add("aba");
    dict.add("acc");
    dict.add("abc");
    dict.add("ccc");
    dict.add("aad");

    String beg = "aaa";
    String end = "abc";
    
    List<String> result = findPath(dict, beg, end);
    System.out.println(result.toString());

    System.out.println("test2");
    ArrayList<String> dict2 = new ArrayList<String>();
    dict2.add("lamp");
    dict2.add("damp");
    dict2.add("himp");
    dict2.add("rine");
    dict2.add("limp");
    dict2.add("lime");
    dict2.add("like");
    beg = "damp";
    end = "like";

    result = findPath(dict2, beg, end);
    System.out.println(result.toString());    
  }

  public static LinkedList<String> findPath(ArrayList<String> dict, String beg, String end) {
    if (dict == null || beg == null || end == null)
      return null;

    HashMap<String, String> parents = new HashMap<String, String>();
    boolean[] visited = new boolean[dict.size()];
    
    LinkedList<String> q = new LinkedList<String>();
    q.add(beg);
    
    boolean escape = false;

    // search through node's nbrs
    while(!q.isEmpty() && !escape) {
      String n = q.remove();
      
      for (int i = 0; i < dict.size(); i++) {
        //System.out.println(str + compareStrings(n, str));
        String str = dict.get(i);
        if (!visited[i] && compareStrings(n, str) && str != beg) {
         
          q.add(str);

          // put in child, parent
          parents.put(str, n);  
          visited[i] = true;
        
          if (str == end) {
            escape = true;
            break;
          }
        
        }
      }
    }
    
    LinkedList<String> result = new LinkedList<String>();
    
    String str = end;
    
    while(parents.containsKey(str)) {
      result.addFirst(str);
      str = parents.get(str);
    }
    result.addFirst(str);
    
    return result;
    
   
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
