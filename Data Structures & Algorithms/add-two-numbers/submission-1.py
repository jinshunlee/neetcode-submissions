# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur = head = None
        overflow = 0

        while l1 or l2 or overflow:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            summed = l1_val + l2_val + overflow
            if not head:
                head = ListNode(summed % 10)
                cur = head
            else:
                cur.next = ListNode(summed % 10)
                cur = cur.next
            overflow = (l1_val + l2_val + overflow) // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head
        
        