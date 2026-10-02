from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # Python min-heap storing negative counts to simulate a max-heap
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()  # Elements: (remaining_neg_count, available_time)

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # Process one unit of task
                if cnt < 0:
                    q.append((cnt, time + n))

            # If the oldest task in cooldown is ready, push back to heap
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time