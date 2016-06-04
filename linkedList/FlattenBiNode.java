/* Consider a simple node-like data structure called BiNode, which has pointers to two other nodes.
 * The data structure BiNode could be used to represent both a binary tree or a doubly linked list.
 * Implement a method to convert a BST (implemented with BiNode) into a doubly linked list. The values 
 * should be kept in order and operations performed in place. */
import java.util.LinkedList;

public class FlattenBiNode {
    public static void main(String[] args) {
        BiNode n25 = new BiNode(25);
        BiNode head = n25;
        BiNode n13 = new BiNode(13);
        BiNode n5 = new BiNode(5);
        BiNode n4 = new BiNode(4);
        BiNode n41 = new BiNode(41);  
        BiNode n30 = new BiNode(30);
        BiNode n26 = new BiNode(26);
        BiNode n32 = new BiNode(32);
        BiNode n31 = new BiNode(31);
        BiNode n33 = new BiNode(33);
        BiNode n37 = new BiNode(37);
        BiNode n35 = new BiNode(35);

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
        // print BiNode tree
        printLevelOrder(head);
        flattenBiNode(head);
        System.out.println();

        // print flattened list
        printList(head);
    }

    public static void flattenBiNode(BiNode n) {
        if (n == null) {
            return;
        }

        if (n.left != null) {
            BiNode pred = n.left;

            while(pred.right != null) {
                pred = pred.right;
            }

            flattenBiNode(n.left);
            n.left = pred;
            pred.right = n;

        }

        if (n.right != null) {
            BiNode succ = n.right;

            while(succ.left != null) {
                succ = succ.left;
            }

            flattenBiNode(n.right);
            n.right = succ;
            succ.left = n;
        }        
    }

    public static void printList(BiNode n) {
        // find leftmost
        while(n.left != null) {
            n = n.left;
        }

        while(n.right != null) {
            System.out.print(n.data + "->");
            n = n.right;
        }
        System.out.print(n.data + "->null\n");

        while (n != null) {
            System.out.print(n.data + "->");
            n = n.left;
        }
        System.out.print("null\n");
    }

    public static void printLevelOrder(BiNode n) {
        if (n == null)
            return; 

        LinkedList<BiNode> q = new LinkedList<BiNode>();
        q.add(n);

        while (!q.isEmpty()) {
            n = q.removeFirst();

            int leftVal = -1; // representing null value
            int rightVal = -1; // representing null value

            if (n.left != null) {
                leftVal = n.left.data;
                q.add(n.left);
            }

            if (n.right != null) {
                rightVal = n.right.data;
                q.add(n.right);
            }

            System.out.printf("Node: %d, Left: %d, Right: %d\n", n.data, leftVal, rightVal);
        }
    }
}

class BiNode {
    public BiNode left, right;
    public int data;

    public BiNode(int data) {
        this.data = data;
    }
}
