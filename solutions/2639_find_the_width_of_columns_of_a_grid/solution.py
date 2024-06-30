"""
title : 2639_find_the_width_of_columns_of_a_grid.py
create : @tarickali 24/01/03
update : @tarickali 24/01/03
"""

import math


class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        def get_len(x: int) -> int:
            if x == 0:
                return 1
            return math.floor(math.log10(abs(x))) + 1 + (1 if x < 0 else 0)

        width = [0 for _ in range(len(grid[0]))]
        for row in grid:
            for i, x in enumerate(row):
                width[i] = max(width[i], get_len(x))
        return width
