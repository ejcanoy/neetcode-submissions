import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        val = [(math.sqrt(vals[0] * vals[0] + vals[1] * vals[1]), i) for i,vals in enumerate(points)]
        print(val)
        heapq.heapify(val)
        res = []
        for i in range(k):
            res.append(points[heapq.heappop(val)[1]])
        
        return res