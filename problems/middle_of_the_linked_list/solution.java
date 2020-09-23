import java.lang.Math;
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
    public ListNode middleNode(ListNode head) {
        int length = 0;
        ListNode start = head;
        
        while (head != null) {
            length++;
            head = head.next;
        }
        
        int index = 0;
        while (start != null) {
            if (index == Math.ceil(length / 2) && length % 2 != 0) return start;
            else if (index == length / 2) return start;
            index++;
            start = start.next;
        }
        return start;
    }
}