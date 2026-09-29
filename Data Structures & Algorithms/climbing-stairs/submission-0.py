class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [1,2]
        while len(cache) < n:
            cur_len = len(cache)
            cache.append(cache[cur_len - 1] + cache[cur_len - 2])
        return cache[n - 1]
