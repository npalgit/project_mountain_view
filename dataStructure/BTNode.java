package interview.dataStructure;
import java.util.LinkedList;

public class BTNode {
    public BTNode left, right;
    public int data;

    public BTNode(int data) {
        this.data = data;
    }

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
        System.out.println();
    }


    public void printLevelOrder() {
        LinkedList<BTNode> q = new LinkedList<BTNode>();
        q.add(this);

        while (!q.isEmpty()) {
            BTNode n = q.removeFirst();

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


