"""
title : 0695_max_area_of_island.py
create : @tarickali 23/03/31
update : @tarickali 23/03/31
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def neighbors(grid: list[list[int]], i: int, j: int) -> list[tuple[int, int]]:
            N = []
            if i + 1 < len(grid):
                N.append((i + 1, j))
            if i - 1 >= 0:
                N.append((i - 1, j))
            if j + 1 < len(grid[i]):
                N.append((i, j + 1))
            if j - 1 >= 0:
                N.append((i, j - 1))
            return N

        def search(grid: list[list[int]], i: int, j: int) -> set[tuple[int, int]]:
            explored = {(i, j)}
            stack = [(i, j)]
            while len(stack) != 0:
                xr, xc = stack.pop()
                for yr, yc in neighbors(grid, xr, xc):
                    if (yr, yc) in explored or grid[yr][yc] == 0:
                        continue
                    explored |= {(yr, yc)}
                    stack.append((yr, yc))
            return explored

        m = len(grid)
        n = len(grid[0])

        best = 0
        explored = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in explored or grid[i][j] == 0:
                    continue
                component = search(grid, i, j)
                best = max(best, len(component))
                explored |= component
        return best
