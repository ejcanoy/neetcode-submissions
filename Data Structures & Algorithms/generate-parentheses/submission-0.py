class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(l, r, path):
            if l > r:
                return
            if l == 0 and r == 0:
                res.append(path)
                return
            if l > 0:
                backtrack(l - 1, r, path + "(")
            if r > 0:
                backtrack(l, r - 1, path + ")")
        backtrack(n-1,n, "(")
        return res