"""
title : 0289_game_of_life.py
create : @tarickali 23/05/24
update : @tarickali 23/05/24
"""

import copy
import itertools


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def neighbors(i: int, j: int, grid: list[list[int]]) -> list[tuple[int, int]]:
            rows = {i, i - 1, i + 1} - {-1, len(grid)}
            cols = {j, j - 1, j + 1} - {-1, len(grid[i])}
            return list(set(itertools.product(rows, cols)) - {(i, j)})

        def state(i: int, j: int, grid: list[list[int]]) -> int:
            cells = neighbors(i, j, grid)
            count = sum(grid[r][c] for r, c in cells)
            val = 0
            if grid[i][j] == 1:
                if count < 2 or count > 3:
                    val = 0
                else:  # c == 2 or c == 3:
                    val = 1
            else:
                if count == 3:
                    val = 1
                else:
                    val = 0
            return val

        temp = copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = state(i, j, temp)
