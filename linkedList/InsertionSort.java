public class InsertionSort {
    public static ListNode insertionSortList(ListNode head) {
       if (head == null) {
           return null;
       }

       ListNode curr = head;
       ListNode dummy_h = new ListNode(0);
       ListNode hd;
       ListNode tail;
       while (curr != null) {
           hd = dummy_h;
           while (hd != null) {
               if (hd.next == null || curr.val < hd.next.val) {
                    tail = hd.next;
                    hd.next = curr;
                    curr = curr.next;
                    hd.next.next = tail;
                    break;
               }
               hd = hd.next;
           }

       }

       return dummy_h.next;
    }

    public static void main(String[] args) {
       ListNode l5 = new ListNode(5);
       ListNode l3 = new ListNode(3);
       ListNode l7 = new ListNode(7);
       ListNode l9 = new ListNode(9);
       ListNode l1 = new ListNode(1);
       ListNode l0 = new ListNode(0);
       ListNode l8 = new ListNode(8);

       l5.next = l3;
       l3.next = l7;
       l7.next = l9;
       l9.next = l1;
       l1.next = l0;
       l0.next = l8;

       ListNode rslt = insertionSortList(l5);

       while (rslt != null) {
           System.out.print(rslt.val);
           System.out.print("->");
           rslt = rslt.next;
       }
       System.out.println();
     }
}


class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

