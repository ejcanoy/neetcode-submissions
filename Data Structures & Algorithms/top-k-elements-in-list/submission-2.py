import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = {}
        for num in nums:
            if not num in values:
                values[num] = 0
            values[num] += 1

        heap = []

        for key in values:
            heapq.heappush(heap,(values[key] * -1, key))
        
        print(heap)
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

