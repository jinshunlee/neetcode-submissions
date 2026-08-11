# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        lst = prev

        count = 1
        prev = None
        cur = lst

        while count < n:
            prev = cur
            count += 1
            cur = cur.next

        if prev is None:
            lst = cur.next
        else:
            prev.next = cur.next

        prev = None

        cur = lst


        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev






        