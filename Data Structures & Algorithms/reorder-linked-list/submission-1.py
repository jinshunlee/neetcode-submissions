# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head
        a = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        b = slow.next
        slow.next = None

        prev = None

        while b:
            nxt = b.next
            b.next = prev
            prev = b
            b = nxt
        b = prev   

        while b:
            a_next = a.next
            b_next = b.next
            a.next = b
            b.next = a_next
            a = a_next
            b = b_next
      