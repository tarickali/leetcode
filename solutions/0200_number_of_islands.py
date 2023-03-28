"""
title : 0200_number_of_islands.py
create : @tarickali 23/03/28
update : @tarickali 23/03/28
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def neighbors(grid: list[list[int]], r: int, c: int) -> list[tuple[int, int]]:
            N = []
            if r + 1 < len(grid):
                N.append((r + 1, c))
            if r - 1 >= 0:
                N.append((r - 1, c))
            if c + 1 < len(grid[r]):
                N.append((r, c + 1))
            if c - 1 >= 0:
                N.append((r, c - 1))
            return N

        def explore_island(grid, i, j) -> set[tuple[int, int]]:
            stack = [(i, j)]
            explored = {(i, j)}
            while len(stack) != 0:
                ur, uc = stack.pop()
                for vr, vc in neighbors(grid, ur, uc):
                    if (vr, vc) in explored:
                        continue
                    if grid[vr][vc] == "1":
                        stack.append((vr, vc))
                        explored.add((vr, vc))
            return explored

        m, n = len(grid), len(grid[0])
        num_islands = 0
        explored = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in explored or grid[i][j] == "0":
                    continue
                explored |= explore_island(grid, i, j)
                num_islands += 1
        return num_islands
