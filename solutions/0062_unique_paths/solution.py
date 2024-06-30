"""
title : 0062_unique_paths.py
create : @tarickali 23/03/14
update : @tarickali 23/03/14
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]
        memo[:][0] = [1] * m
        memo[0][:] = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[m - 1][n - 1]
