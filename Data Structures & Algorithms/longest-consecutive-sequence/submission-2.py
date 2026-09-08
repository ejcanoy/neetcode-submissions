import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        heap = []
        for num in nums:
            heapq.heappush(heap, num)


        maxlength = 1
        length = 1
        prev = heap[0] 
        while heap:
            print(length, heap[0], prev + 1)
            if heap[0] == prev:
                heapq.heappop(heap)
                continue
            if heap[0] == prev + 1:
                length += 1
            else:
                maxlength = max(maxlength, length)
                length = 1
            prev = heap[0]
            heapq.heappop(heap)

        return max(maxlength, length)