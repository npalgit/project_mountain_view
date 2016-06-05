/* You are given a binary tree in which each node contains a value. Design an algorithm to print all
 * paths which sum to a given value. The path does not need to start or end at the root or a leaf, but it must 
 * go in a straight line down. */
package interview.trees;
import java.util.LinkedList;
import interview.dataStructure.BTNode;

class FindSum {	
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
        System.out.println("Paths add up to target: 6");
        LinkedList<LinkedList<Integer>> result = findSumPath(head, 6);
        System.out.println("Paths add up to target: 4");
        result = findSumPath(head, 4);
    }

    /**  Find number of paths sum to a target value. int[0] = numPath to target, int[1] = currPathValue. */
    public static LinkedList<LinkedList<Integer>> findSumPath(BTNode n, int target) {
        if (n.data == target)
            System.out.println("[" + n.data + "]");

        if (n.left == null && n.right == null) {
            LinkedList<Integer> l = new LinkedList<Integer>();
            l.add(n.data);

            LinkedList<LinkedList<Integer>> lists = new LinkedList<LinkedList<Integer>>();
            lists.add(l);
            return lists;
        }

        LinkedList<LinkedList<Integer>> leftLists = new LinkedList<LinkedList<Integer>>();
        if (n.left != null)
            leftLists = findSumPath(n.left, target);

        LinkedList<LinkedList<Integer>> rightLists = new LinkedList<LinkedList<Integer>>();
        if (n.right != null)
            rightLists = findSumPath(n.right, target);

        // The path goes from left to center to right after checking its value, then discarded.
        if (!leftLists.isEmpty() && !rightLists.isEmpty())
            countLCR(leftLists, rightLists, n.data, target);

        LinkedList<LinkedList<Integer>> newLists = new LinkedList<LinkedList<Integer>>();

        for (LinkedList<Integer> list : leftLists) {
            list.addFirst(n.data);

            if (sumPath(list) == target)
                System.out.println(list.toString());

            newLists.add(list);
        }

        for (LinkedList<Integer> list : rightLists) {
            list.addFirst(n.data);

            if (sumPath(list) == target)
                System.out.println(list.toString());

            newLists.add(list);
        }

        LinkedList<Integer> newlist = new LinkedList<Integer>();
        newlist.add(n.data);
        newLists.add(newlist);

        return newLists;
    }

    public static int sumPath(LinkedList<Integer> path) {
        int sum = 0;
        for (Integer i : path) {
            sum += i;
        }

        return sum;
    }

    /** Count if left to center to right yields the target value. */
    public static void countLCR(LinkedList<LinkedList<Integer>> lists1, 
        LinkedList<LinkedList<Integer>> lists2, int data, int target) {
        for (LinkedList<Integer> list : lists1) {
            LinkedList<Integer> templ = new LinkedList<Integer>();
            templ.addAll(list);
            templ.add(data);
 
            for (LinkedList<Integer> list2 : lists2) {
                templ.addAll(list2);

                if (sumPath(templ) == target)
                    System.out.println(templ.toString());
            }

        }

    }
}
