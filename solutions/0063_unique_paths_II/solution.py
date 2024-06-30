"""
title : 0062_unique_paths.py
create : @tarickali 23/03/14
update : @tarickali 23/03/14
"""


class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        memo = [[0] * n for i in range(m)]

        for i in range(m):
            if grid[i][0] == 1:
                break
            memo[i][0] = 1
        for j in range(n):
            if grid[0][j] == 1:
                break
            memo[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j]:
                    continue
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[m - 1][n - 1]
