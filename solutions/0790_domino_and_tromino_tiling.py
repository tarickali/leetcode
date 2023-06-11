"""
title : 0790_domino_and_tromino_tiling.py
create : @tarickali 23/06/10
update : @tarickali 23/06/10
"""


class Solution:
    def numTilings(self, n: int) -> int:
        memo = {}

        def recurse(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i > n or j > n:
                return 0

            if i == j == n:
                res = 1
            elif i > j:
                res = recurse(i, j + 2) + recurse(i + 1, j + 2)
            elif i < j:
                res = recurse(i + 2, j) + recurse(i + 2, j + 1)
            else:
                res = (
                    recurse(i + 1, j + 1)
                    + recurse(i + 2, j + 1)
                    + recurse(i + 2, j + 2)
                    + recurse(i + 1, j + 2)
                )
            memo[(i, j)] = res
            return res

        return recurse(0, 0) % (10**9 + 7)
