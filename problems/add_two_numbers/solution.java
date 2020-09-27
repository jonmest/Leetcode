/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode next = dummy;
        
        int carry = 0;
        while (l1 != null || l2 != null) {
            int x = 0, y = 0, sum = 0;
            x = (l1 != null) ? l1.val : 0;
            y = (l2 != null) ? l2.val : 0;
            sum = carry + x + y;
            carry = sum / 10;
            
            ListNode temp = new ListNode(sum % 10);
            next.next = temp;
            next = temp;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        if (carry > 0) next.next = new ListNode(carry);
        return dummy.next;
    }

}