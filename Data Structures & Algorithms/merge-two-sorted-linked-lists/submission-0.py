# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = list1, list2
        dummy = ListNode(-1, None)
        cur = dummy
        while c1 and c2:
            if c1.val < c2.val:
                cur.next = c1
                c1 = c1.next
            else:
                cur.next = c2
                c2 = c2.next
            cur = cur.next
        
        if c1:
            cur.next = c1
        else:
            cur.next = c2

        return dummy.next
