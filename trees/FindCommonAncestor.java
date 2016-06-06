/* Given a binary tree, find the first common ancestor of two nodes in a binary tree. Do this in place. */
package interview.trees;
import interview.dataStructure.BTNode;

public class FindCommonAncestor {

    public static void main(String[] args) {
        /*    3
             /\
            4    5
           /\     \
          7  8     9
            /     /
          11     10 
                  \
                  12
        */

        BTNode n3 = new BTNode(3);
        BTNode n4 = new BTNode(4);
        BTNode n5 = new BTNode(5);
        BTNode n7 = new BTNode(7);
        BTNode n8 = new BTNode(8);
        BTNode n9 = new BTNode(9);
        BTNode n10 = new BTNode(10);
        BTNode n11 = new BTNode(11);
        BTNode n12 = new BTNode(12);

        n3.left = n4;
        n3.right = n5;
        n4.left = n7;
        n4.right = n8;
        n8.left = n11;
        n5.right = n9;
        n9.left = n10;
        n10.right = n12;

        BTNode ancestor = new BTNode(-1);

        findCommonAncestor(n3, n7, n11, ancestor);
        System.out.printf("Common ancestor is: n%d\n", ancestor.data);

        CommonAncestor ca = findCommonAncestorElegant(n3, n7, n11);
        System.out.printf("Found Ancestor: %s. Common ancestor is: n%d\n", ca.isAncestor, ca.node.data);

        findCommonAncestor(n3, n11, n12, ancestor);
        System.out.printf("Common ancestor is: n%d\n", ancestor.data);

        ca = findCommonAncestorElegant(n3, n11, n12);
        System.out.printf("Found Ancestor: %s. Common ancestor is: n%d\n", ca.isAncestor, ca.node.data);



    }

    /** Find common ancestor by modifying the content of the commonAncestor node passed in. */
    public static int findCommonAncestor(BTNode n, BTNode t1, BTNode t2, BTNode commonAncestor) {
        if (n == null || t1 == null || t2 == null)
            return -1;

        if (n.data == t1.data && t2.data == t1.data) {
            commonAncestor.data = n.data;
            return 1;
        }

        int lhs = findCommonAncestor(n.left, t1, t2, commonAncestor);
        int rhs = findCommonAncestor(n.right, t1, t2, commonAncestor);

        if ((n.data == t1.data || n.data == t2.data) && (lhs == 0 || rhs == 0)) {
                commonAncestor.data = n.data;
                return 1;
                
        }

        
        if (lhs == 0 && rhs ==0) {
            commonAncestor.data = n.data;
            return 1;
        }


        if (lhs == 1 || rhs ==1)
            return 1;

        if ((n.data == t1.data || n.data == t2.data) || (lhs == 0 || rhs == 0))
            return 0;


        return -1;
    }


    /** Find common ancestor by returning a new CommonAncestor object. */
    public static CommonAncestor findCommonAncestorElegant(BTNode n, BTNode t1, BTNode t2) {
        if (n == null || t1 == null || t2 == null)
            return new CommonAncestor();

        CommonAncestor lhs = findCommonAncestorElegant(n.left, t1, t2);
        CommonAncestor rhs = findCommonAncestorElegant(n.right, t1, t2);

        if (lhs.node != null && rhs.node != null) {
            return new CommonAncestor(n, true);
        } else if (n == t1 || n == t2) {
            boolean isAncestor = (lhs.node != null || rhs.node != null)? true : false;
            return new CommonAncestor(n, isAncestor);
        } 

        return (lhs.node != null)? lhs : rhs;
    }
}

class CommonAncestor {
    public BTNode node;
    boolean isAncestor = false;

    public CommonAncestor() {}

    public CommonAncestor(BTNode node, boolean isAncestor) {
        this.node = node;
        this.isAncestor = isAncestor;
    }

}

