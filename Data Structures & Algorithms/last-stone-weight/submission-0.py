import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = [-val for val in stones]
        heapq.heapify(res)
        while len(res) >= 2:
            print(res)
            n1, n2 = heapq.heappop(res), heapq.heappop(res)
            total = abs((-n1) - (-n2))
            if total != 0:
                heapq.heappush(res, -total)
        
        return -res[0] if res else 0