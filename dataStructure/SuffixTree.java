package interview.dataStructure;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.ArrayList;

/** Suffix Tree representation of a string. */
public class SuffixTree {
    private String string;
    private SuffixTreeNode head = new SuffixTreeNode();

    public SuffixTree(String str) {
        string = str;

        SuffixTreeNode node;
        for (int i = 0; i < string.length(); i++) {
            node = head;
            for (int j = i; j < string.length(); j++) {
                Character c = string.charAt(j);
                if (!node.containsChild(c)) {
                    node.addChild(c, new SuffixTreeNode(c));
                }
                node = node.getChild(c);
            }
        }

    }

    /** Return the String the SuffixTree contains */
    public String getString() {
        return string;
    }

    /** Check to see if the tree contains substring */
    public boolean containsSubstring(String str) {
        SuffixTreeNode node = head;
        Character c;

        for (int i = 0; i < str.length(); i++) {
            c = str.charAt(i);

            if (node.containsChild(c))
                node = node.getChild(c);
            else
                return false;
        }
        return true;

    }

    /** Print out the tree in Breadth First Search Fashion. 
      * NOTE: the serialized orders are a little off*/
    public void print() {
        SuffixTreeNode node = head;
        // BFS style print elements out
        LinkedList<SuffixTreeNode> q = new LinkedList<SuffixTreeNode>();
        q.add(head);

        while (!q.isEmpty()) {
            SuffixTreeNode n = q.removeFirst();
            System.out.print("Node: " + n.getValue() + " ");
            System.out.print("Children: ");

            for (SuffixTreeNode child : n.getChildren().values()) {
                q.add(child);
                System.out.print(child.getValue() + ", ");
            }

            System.out.println();
        }

    }

    public static void main(String[] args) {
        String str = "abaaba";
        SuffixTree stree = new SuffixTree(str);
        System.out.println(stree.containsSubstring("hello"));
        System.out.println(stree.containsSubstring("ab"));
        System.out.println(stree.containsSubstring("aa"));
        System.out.println(stree.containsSubstring("a"));
        System.out.println(stree.containsSubstring("aaba"));
        System.out.println();
        str = "helloworld";
        stree = new SuffixTree(str);
        System.out.println(stree.containsSubstring("hello"));
        System.out.println(stree.containsSubstring("owo"));
        System.out.println(stree.containsSubstring("rld"));
        System.out.println(stree.containsSubstring("dl"));
        System.out.println(stree.containsSubstring("l"));
        System.out.println(stree.containsSubstring("owor"));
        System.out.println(stree.containsSubstring("lwo"));

    }



}

/** Denotes a suffix tree node. */
class SuffixTreeNode {
    private Character c;
    private HashMap<Character, SuffixTreeNode> children = new HashMap<Character, SuffixTreeNode>();

    /** Constructor */
    public SuffixTreeNode() {}

    /** Constructor takes in a character value */
    public SuffixTreeNode(Character c) {
        this.c = c;
    }

    /** Add a child to the tree. */
    public void addChild(Character c, SuffixTreeNode child) {
        children.put(c, child);
    }

    /** Return a child given the character */
    public SuffixTreeNode getChild(Character c) {
        if (containsChild(c))
            return children.get(c);
        else
            return null;
    }

    /** Check to see if the node contains a certain child look up using the character. */
    public boolean containsChild(Character c) {
        if (children.containsKey(c))
            return true;
        return false;
    }

    /** Re-set the children to a different collection (HashMap) of children. */
    public void setChildren(HashMap<Character, SuffixTreeNode> children) {
        this.children = children;
    }  

    /** Return the value of the node. */
    public Character getValue() {
        return c;
    }

    /** Return the collection of children.  */
    public HashMap<Character, SuffixTreeNode> getChildren() {
        return children;
    }

}
