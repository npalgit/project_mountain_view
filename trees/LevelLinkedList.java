/* Given a binary tree, design an algorithm which creates a linked list of al the nodes at each depth.
 * (e.g. if you have a tree with depth D, you'll have D linkedLists) */
package interview.trees;
import interview.dataStructure.BTNode;
import java.util.LinkedList;
import java.util.ArrayList;

class LevelLinkedList {
    public static void main(String[] args) {
        BTNode n0 = new BTNode(0);
        BTNode head = n0;

        BTNode n1 = new BTNode(1);
        BTNode n2 = new BTNode(2);
        BTNode n3 = new BTNode(3);
        BTNode n4 = new BTNode(4);
        BTNode n9 = new BTNode(9);
        BTNode nn3 = new BTNode(-3);
        BTNode nn2 = new BTNode(-2);

        n0.left = n9;
        n9.right = nn3;
        n0.right = n3;
        n3.left = n1;
        n3.right = n4;
        n4.left = n2;
        n2.left = nn2;

        head.printLevelOrder();
        ArrayList<LinkedList<Integer>> lists = new ArrayList<LinkedList<Integer>>();
        createLevelLinkedList(head, lists, 0);

        for (LinkedList<Integer> list : lists) {
            System.out.println(list.toString());
        }
    }

    /** Create linkedlist at each depth. */
    public static void createLevelLinkedList(BTNode n, ArrayList<LinkedList<Integer>> lists, int level) {
        if (n == null)
            return;

        if (lists.size() <= level) {
            LinkedList<Integer> l = new LinkedList<Integer>();
            l.add(n.data);
            lists.add(l);
        } else {
            LinkedList<Integer> l = lists.get(level);
            l.add(n.data);
        }

        createLevelLinkedList(n.left, lists, level+1);
        createLevelLinkedList(n.right, lists, level+1);
    }
}
