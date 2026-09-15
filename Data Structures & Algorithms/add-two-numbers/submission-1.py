# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(-1)
        cur = dummy

        while l1 and l2:
            total = carry + l1.val + l2.val
            cur.next = ListNode(total % 10)
            carry = total // 10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            total = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            cur.next = ListNode(total)
            cur = cur.next
            l1 = l1.next

        while l2:
            total = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            cur.next = ListNode(total)
            cur = cur.next
            l2 = l2.next
            
        if carry > 0:
            cur.next = ListNode(carry)

        return dummy.next