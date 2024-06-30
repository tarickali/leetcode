"""
title : 0064_minimum_path_sum.py
create : @tarickali 23/03/19
update : @tarickali 23/03/19
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[0] * n for _ in range(m)]

        memo[0][0] = grid[0][0]
        for i in range(1, m):
            memo[i][0] = memo[i - 1][0] + grid[i][0]
        for j in range(1, n):
            memo[0][j] = memo[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = min(memo[i - 1][j], memo[i][j - 1]) + grid[i][j]
        return memo[m - 1][n - 1]
