/* Remove duplicates from a given linkedList. */
package interview.linkedList;
import interview.dataStructure.LinkedListNode;
import java.util.HashSet;

class RemoveDuplicates {

    public static void main(String[] args) {
        LinkedListNode<String> n0 = new LinkedListNode<String>("P");
        LinkedListNode<String> n1 = new LinkedListNode<String>("O");
        LinkedListNode<String> n2 = new LinkedListNode<String>("L");
        LinkedListNode<String> n3 = new LinkedListNode<String>("L");
        LinkedListNode<String> n4 = new LinkedListNode<String>("O");
        LinkedListNode<String> n5 = new LinkedListNode<String>("W");
        LinkedListNode<String> n6 = new LinkedListNode<String>("U");
        LinkedListNode<String> n7 = new LinkedListNode<String>("P");
        
        n0.setNext(n1);
        n1.setNext(n2);
        n2.setNext(n3);
        n3.setNext(n4);
        n4.setNext(n5);
        n5.setNext(n6);
        n6.setNext(n7);

        n0.printList();

        removeDuplicatesHash(n0);
        n0.printList();

    }

    /** remove duplicates using O(1) space */
    public static void removeDuplicates(LinkedListNode<String> head) {
        LinkedListNode<String> n1 = head;
        LinkedListNode<String> n2;

        while (n1 != null) {

            n2 = n1;
            while (n2.getNext() != null) {
                if (n1.getItem().equals(n2.getNext().getItem())) {
                    n2.setNext(n2.getNext().getNext());
                }

                if (n2.getNext() != null)
                    n2 = n2.getNext();
            }

            n1 = n1.getNext();
        }

    }

    /** remove duplicates using hash space */
    public static void removeDuplicatesHash(LinkedListNode<String> n) {
        if (n == null)
            return;

        HashSet<String> set = new HashSet<String>();
        set.add(n.getItem());

        while (n.getNext() != null) {
            if (!set.contains(n.getNext().getItem())) {
                set.add(n.getNext().getItem());
            } else {
                n.setNext(n.getNext().getNext());
            }

            if (n.getNext() != null)
                n = n.getNext();
        }

    }
    


}
