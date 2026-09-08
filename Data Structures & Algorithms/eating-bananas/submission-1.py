class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            count = sum(math.ceil(pile / k) for pile in piles)
            print(count, k)
            print()
            if count <= h:
                return True
            return False

        piles.sort()
        res = piles[-1]
        l = 1
        r = piles[-1]
        while l <= r:
            m = (r - l) // 2 + l
            if canFinish(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res
