class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        res = []
        def dfs(path, digits):
            if not digits:
                if path != "":
                    res.append(path)
                return
            print(digits[0])
            letters = combos[int(digits[0])]
            for letter in letters:
                dfs(path + letter, digits[1:])
        
        dfs("", digits)
        return res

