class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Counts = {}
        s2Counts = {}
        for c in s1:
            if c not in s1Counts:
                s1Counts[c] = 0
            s1Counts[c] += 1
        
        l = 0
        for i in range(len(s2)):
            if s2[i] not in s2Counts:
                s2Counts[s2[i]] = 0
            s2Counts[s2[i]] += 1

            while i - l > len(s1) - 1:
                s2Counts[s2[l]] -= 1
                if s2Counts[s2[l]] == 0:
                    del s2Counts[s2[l]]
                l += 1
            
            if s1Counts == s2Counts:
                return True
            
        return False