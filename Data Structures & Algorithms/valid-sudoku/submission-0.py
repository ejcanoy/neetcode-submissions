class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                seen["row" + str(r)] = set()
                seen["col" + str(c)] = set()
                seen[str(r // 3)+str(c // 3)] = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val != ".":
                    if val in seen["row" + str(r)] or val in seen["col" + str(c)] or val in seen[str(r//3) + str(c//3)]:
                        print(val)
                        print(f"{r}\n{c}\n{r//3}\n{c//3}\n{seen}")

                        return False
                    seen["row" + str(r)].add(val)
                    seen["col" + str(c)].add(val)
                    seen[str(r//3) + str(c//3)].add(val)
        
        return True


    