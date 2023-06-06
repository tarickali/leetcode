"""
title : 2352_equal_row_and_column_pairs.py
create : @tarickali 23/05/06
update : @tarickali 23/05/06
"""

from collections import Counter


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = {}
        cols = {}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                rows[i] = rows.get(i, ()) + (grid[i][j],)
                cols[j] = cols.get(j, ()) + (grid[i][j],)

        rows = Counter(rows.values())
        cols = Counter(cols.values())

        return sum(rows[cnt] * cols[cnt] for cnt in set(rows) & set(cols))
