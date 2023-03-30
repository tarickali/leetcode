"""
title : 1351_count_negative_numbers_in_a_sorted_matrix.py
create : @tarickali 23/03/30
update : @tarickali 23/03/30
"""


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] < 0:
                    count += 1
                else:
                    continue
        return count

    def countNegatives(self, grid: list[list[int]]) -> int:
        def search(row: list[int], edge: int) -> int:
            n = len(row)
            if edge == n:
                return edge
            l = edge
            r = n - 1
            while l <= r:
                m = l + (r - l) // 2
                if row[m] >= 0:
                    l = m + 1
                else:
                    r = m - 1
            return l

        m = len(grid)
        n = len(grid[0])
        edge = 0
        count = 0
        for i in range(m - 1, -1, -1):
            edge = search(grid[i], edge)
            count += n - edge
        return count
