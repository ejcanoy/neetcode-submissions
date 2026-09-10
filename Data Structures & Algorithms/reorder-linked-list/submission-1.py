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
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        cur = slow.next
        slow.next = None
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        print(prev.val, head.val)
        dummy = ListNode(-1, head)
        cur = dummy
        while prev and head:
            cur.next = head
            head = head.next
            cur = cur.next
            cur.next = prev
            prev = prev.next
            cur = cur.next
        
        if head:
            cur.next = head
        elif prev:
            cur.next = prev
        head = dummy.next