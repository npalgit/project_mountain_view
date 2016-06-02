/* 
A persistent data structure is a data structure that always preserves 
all previous versions of itself when it is modified. Similarly, a persistent
stack is a stack that preverses all its previous copies.
*/
package interview.dataStructure;
import interview.dataStructure.LinkedListNode;
import java.util.HashMap;

/** Persistent stack that keeps track of all versions of the stack. The stack is implemented following 
  * these rules to reduce the number of stack elements that are copied.
  * 1. pop then push, make a copy of previous version.
  * 2. push then push, don't make a copy of previous version 
  * 3. go back to an old version then push, make a copy of previous version.
  * 4. go back to an old version then pop, don't make a copy of previous version.
  */
class PersistentStack {
    public HashMap<Integer, LinkedListNode<Integer>> record = new HashMap<Integer, LinkedListNode<Integer>>();
    private Integer totalVersion = new Integer(0);
    private Integer currentVersion = new Integer(0);
    private PrevInstr prevInstr;

    private LinkedListNode<Integer> curr_stack;

    public boolean isEmpty() {
        if (curr_stack == null)
            return true;

        return false;
    }

    /** Go to a certain version of the stack. Return true if that version exists. And false
     * if the version is invalid. */
    public boolean goToVersion(Integer version) {
        
        if (record.containsKey(version)) {
            curr_stack = record.get(version);
            currentVersion = version;
            prevInstr = PrevInstr.GOTOVERSION;
            return true;
        }

        return false;
    }

    /** Return the current version that the stack is on. */
    public Integer currentVersion() {
        return currentVersion;
    }

    /** Return the first item on the current stack. */
    public Integer peek() {
        return curr_stack.getItem();
    }

    /** Print the whole stack top to bottom with version number as well. */
    public void print() {
        System.out.print("v" + currentVersion + " : ");
        curr_stack.printList();
    }

    /** Push a value onto the current stack. */
    public void push(Integer value) {
        if (value == null)
            return;

        LinkedListNode<Integer> head = new LinkedListNode<Integer>(value);
   
        //Create a new copy of curr_stack
        if (prevInstr == PrevInstr.POP || prevInstr == PrevInstr.GOTOVERSION) {
            LinkedListNode<Integer> copyStack = copyStack(curr_stack);
            head.setNext(copyStack);
        } else {
            head.setNext(curr_stack);
       }

        curr_stack = head;
        prevInstr = PrevInstr.PUSH;

        record.put(++totalVersion, head);
    }

    /** Pop a value off the current stack. */
    public Integer pop() {
        if (curr_stack == null)
            return null;

        Integer result = curr_stack.getItem();
        curr_stack = curr_stack.getNext();
        prevInstr = PrevInstr.POP;

        if (curr_stack != null)
            record.put(++totalVersion, curr_stack);

        return result;
    }

    /** Make a new copy of the stack content. */
    public LinkedListNode<Integer> copyStack(LinkedListNode<Integer> node) {
        if (node == null)
            return null;

        LinkedListNode<Integer> head = new LinkedListNode<Integer>(node.getItem());
        node = node.getNext();

        LinkedListNode<Integer> copyNode;

        if (node != null) {
            copyNode = new LinkedListNode<Integer>(node.getItem());
            head.setNext(copyNode);
        } else {
            return head;
        }
                 

        while (node.getNext() != null) {
            Integer value = node.getNext().getItem();
            copyNode.setNext(new LinkedListNode<Integer>(value));
            copyNode = copyNode.getNext();
            node = node.getNext();
        }

        return head;
    }

    /** Print all versions and content of this log. */
    public void versionLog() {
        System.out.println("-- all versions --");
        for (Integer v : record.keySet()) {
            System.out.print("v" + v + " : ");
            record.get(v).printList();
        }

    }

    /** Signifies different kind of instruction the stack could perform. */
    private enum PrevInstr {
        PUSH, POP, GOTOVERSION
    }

    public static void main(String args[]) {
        PersistentStack stack = new PersistentStack();

        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.versionLog();

        stack.goToVersion(1);
        stack.push(4);
        stack.versionLog();

        stack.goToVersion(1);
        stack.push(5);
        stack.push(6);
        stack.push(7);
        stack.push(8);
        stack.versionLog();

        stack.goToVersion(2);
        stack.push(9);
        stack.push(10);
        stack.push(11);
        stack.push(12);
        stack.versionLog();

        stack.goToVersion(4);
        stack.pop();
        stack.pop();
        stack.pop();

        stack.push(14);
        stack.push(15);
        stack.versionLog();

        stack.pop();
        stack.push(17);
        stack.versionLog();

        stack.goToVersion(11);
        stack.pop();
        stack.pop();
        stack.pop();
        stack.pop();
        stack.push(22);
        stack.push(23);
        stack.versionLog();
    }
}
    
