
/* Given a node n in a BTnary search tree, find the successor of n in the most efficent way.
   What if you don't have a pointer to its parent? */
package interview.trees;
import interview.dataStructure.BTNode;

class BSTSuccessorSearch {
    public static void main(String[] args) {
        BTNode n25 = new BTNode(25);
        BTNode head = n25;
        BTNode n13 = new BTNode(13);
        BTNode n5 = new BTNode(5);
        BTNode n4 = new BTNode(4);
        BTNode n41 = new BTNode(41);  
        BTNode n30 = new BTNode(30);
        BTNode n26 = new BTNode(26);
        BTNode n32 = new BTNode(32);
        BTNode n31 = new BTNode(31);
        BTNode n33 = new BTNode(33);
        BTNode n37 = new BTNode(37);
        BTNode n35 = new BTNode(35);

        n25.left = n13;
        n25.right = n41;

        n13.left = n5;
        n5.left = n4;

        n41.left = n30;

        n30.left = n26;
        n30.right = n32;

        n32.left = n31;
        n32.right = n33;
        n33.right = n37;
        n37.left = n35;
        // print BTNode tree
        head.printLevelOrder();
        BTNode succ = findBSTSuccessor(head, n4);
        System.out.println("Successor: " + succ.data);

        succ = findBSTSuccessor(head, n25);
        System.out.println("Successor: " + succ.data);

        succ = findBSTSuccessor(head, n13);
        System.out.println("Successor: " + succ.data);

        succ = findBSTSuccessor(head, n32);
        System.out.println("Successor: " + succ.data);

        succ = findBSTSuccessor(head, n35);
        System.out.println("Successor: " + succ.data);

        succ = findBSTSuccessor(head, n37);
        System.out.println("Successor: " + succ.data);

        succ = findBSTSuccessor(head, n41);
        System.out.println("Successor: " + succ);
    }

    /** Find the BTnary search tree Successor. */
    public static BTNode findBSTSuccessor(BTNode root, BTNode n) {
        if (n == null)
            return null;

        if (n.right != null) {
            n = n.right;
            while (n.left != null) {
                n = n.left;
            }
            return n;
        } else {
            BTNode max = null;
            BTNode temp = root;

            while(temp != null) {
                if (temp.data == n.data) {
                    return max;
                } else if (temp.data < n.data) {
                    temp = temp.right;
                } else {
                    max = temp;
                    temp = temp.left;
                }
            }

        }
        return null;
    }
}
