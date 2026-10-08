import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Seed the heap with the first node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(-1)
        cur = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next