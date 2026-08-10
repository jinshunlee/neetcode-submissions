class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head.next
        a = head

        # Find the end of the first half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list
        b = slow.next
        slow.next = None

        # Reverse the second half
        prev = None

        while b:
            nxt = b.next
            b.next = prev
            prev = b
            b = nxt

        b = prev

        # Merge both halves
        while b:
            a_next = a.next
            b_next = b.next

            a.next = b
            b.next = a_next

            a = a_next
            b = b_next
        