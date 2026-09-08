from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])

        # 1. Binary search to identify the correct row
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        else:
            return False  # Target is completely outside matrix bounds

        target_row = (top + bot) // 2

        # 2. Binary search within the identified row
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False