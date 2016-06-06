package interview.dataStructure;
public class LinkedListNode<E> {
    private E item;
    private LinkedListNode<E> next;

    public LinkedListNode(E item) {
        this.item = item;
    }

    public LinkedListNode() {}

    public void setItem(E item) {
        this.item = item;
    }

     public E getItem() {
        return this.item;
    }

    public void setNext(LinkedListNode<E> node) {
        next = node;
    }

    public LinkedListNode<E> getNext() {
        return this.next;
    }

    public void printNode() {
        System.out.println(this.item);
    }

    public void printList() {
        LinkedListNode temp = this;

        while (temp != null) {
            System.out.print(temp.getItem().toString() + "->");
            temp = temp.getNext();
        }
        System.out.println("null");
    }

    public static void main(String args[]) {

        LinkedListNode<Integer> n = new LinkedListNode<Integer>(new Integer(1));
        LinkedListNode<Integer> n1 = new LinkedListNode<Integer>(new Integer(2));
        LinkedListNode<Integer> n2 = new LinkedListNode<Integer>(new Integer(3));
        
        n.setNext(n1);
        n1.setNext(n2);

        n.printList();

    }


}
