from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        search = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(r, c, i):
            # Base case: matched all letters
            if i == len(word) - 1:
                return True

            # Mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # Check all 4 directions
            for vals in search:
                new_r = r + vals[0]
                new_c = c + vals[1]
                # Lower and upper bound checks + character match check
                if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and board[new_r][new_c] == word[i + 1]:
                    if dfs(new_r, new_c, i + 1):
                        board[r][c] = temp  # Restore before returning
                        return True

            # Backtrack
            board[r][c] = temp
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False