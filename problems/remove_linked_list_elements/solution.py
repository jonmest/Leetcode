# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if not(head):
            return
        
        node = head
        while node:
            temp = node.next
            while temp and temp.val == val: temp = temp.next
            if node.val == val:
                head, node = temp, temp
            elif node.next!=temp:
                node.next, node = temp, temp
            else:
                node = node.next
                
        return head