package interview.linkedList;
import java.util.Arrays;
import interview.dataStructure.LinkedListNode;

/* Reverse a linked list. */
class ReverseLinkedList {
    private static LinkedListNode<Integer> ret_head = new LinkedListNode<Integer>();
    public static void main(String[] args) {
       

       LinkedListNode<Integer> head = new LinkedListNode<Integer>(1);
       LinkedListNode<Integer> node = new LinkedListNode<Integer>(2);
       head.setNext(node);

       node.setNext(new LinkedListNode<Integer>(3));
       node = node.getNext();
       node.setNext(new LinkedListNode<Integer>(4));
       node = node.getNext();
       node.setNext(new LinkedListNode<Integer>(5));

       head.printList();
       ret_head.printList();
    }

    private static LinkedListNode<Integer> reverse(LinkedListNode<Integer> node) {
        if (node.getNext() == null) {
            ret_head = node;
            return node;
        }

        LinkedListNode<Integer> new_n = reverse(node.getNext());
        node.setNext(null);
        new_n.setNext(node);

        return new_n.getNext();
    }
}
