from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # If there are no fresh oranges from the start, 0 minutes are needed
        if fresh == 0:
            return 0

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        turns = 0

        # Only continue as long as there are both rotten oranges to spread AND fresh oranges left
        while q and fresh > 0:
            turns += 1
            cur_level = len(q)

            for _ in range(cur_level):
                r, c = q.popleft()

                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc

                    if (
                        new_r < 0 or new_c < 0 or
                        new_r == ROWS or new_c == COLS or
                        grid[new_r][new_c] != 1
                    ):
                        continue

                    # 1. Mark as rotten in-place
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    q.append((new_r, new_c))

        return turns if fresh == 0 else -1