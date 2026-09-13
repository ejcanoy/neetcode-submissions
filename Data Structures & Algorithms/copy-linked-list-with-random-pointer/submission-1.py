"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        cur = dummy
        head2 = head
        created = {}

        while head:
            newNode = Node(head.val)
            cur.next = newNode
            cur = cur.next
            created[head] = newNode
            head = head.next
            
        cur = dummy.next
        while head2:
            randExist = head2.random
            if randExist:
                cur.random = created[head2.random]
            else:
                cur.random = None
            head2 = head2.next
            cur = cur.next

        return dummy.next