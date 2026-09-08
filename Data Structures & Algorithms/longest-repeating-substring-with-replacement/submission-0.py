class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        res = 0
        l = 0
        r = 0
        while r < len(s):
            counts[ord(s[r]) - ord("A")] += 1
            while r - l + 1 - max(counts) > k:
                counts[ord(s[l]) - ord("A")] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res
            


