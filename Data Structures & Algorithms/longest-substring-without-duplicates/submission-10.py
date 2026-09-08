class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = {}
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            if not counts.get(s[r]):
                counts[s[r]] = 0
            counts[s[r]] += 1
            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            r += 1

        return longest