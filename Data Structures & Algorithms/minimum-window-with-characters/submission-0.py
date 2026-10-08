from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        window = Counter(t)
        need = len(window)
        has = 0
        seen = defaultdict(int)

        res_len = float("inf")
        res_range = (-1, -1)

        l = 0
        for r, c in enumerate(s):
            # Expand right
            if c in window:
                seen[c] += 1
                if seen[c] == window[c]:
                    has += 1

            # Contract left while all required characters are satisfied
            while has == need:
                # Update best window found so far
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res_range = (l, r)

                char_left = s[l]
                if char_left in window:
                    seen[char_left] -= 1
                    if seen[char_left] < window[char_left]:
                        has -= 1
                l += 1

        start, end = res_range
        return s[start : end + 1] if res_len != float("inf") else ""