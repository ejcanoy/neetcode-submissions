class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = ""
        
        for i in range(len(strs[0])):
            # Compare character at index i for every string
            for s in strs:
                # 1. If index i exceeds string s's length OR
                # 2. Character at index i in s doesn't match character at index i in strs[0]
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            
            # Correctly indented inside the outer loop
            res += strs[0][i]
             
        return res
                
            
            