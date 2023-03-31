"""
title : 1254_number_of_closed_islands.py
create : @tarickali 23/03/31
update : @tarickali 23/03/31
"""


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def neighbors(grid: list[list[int]], i: int, j: int) -> list[tuple[int, int]]:
            N = []
            N += [(i + 1, j)] if i + 1 < len(grid) else [None]
            N += [(i - 1, j)] if i - 1 >= 0 else [None]
            N += [(i, j + 1)] if j + 1 < len(grid[i]) else [None]
            N += [(i, j - 1)] if j - 1 >= 0 else [None]
            return N

        def search(grid: list[list[int]], i: int, j: int) -> set[tuple[int, int]]:
            explored = {(i, j)}
            stack = [(i, j)]
            closed = True
            while len(stack) != 0:
                xr, xc = stack.pop()
                for y in neighbors(grid, xr, xc):
                    if y == None:
                        closed = False
                        continue
                    yr, yc = y
                    if (yr, yc) in explored or grid[yr][yc] == 1:
                        continue
                    explored |= {(yr, yc)}
                    stack.append((yr, yc))
            return explored, closed

        m = len(grid)
        n = len(grid[0])

        total = 0
        explored = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in explored or grid[i][j] == 1:
                    continue
                component, closed = search(grid, i, j)
                total += closed
                explored |= component
        return total
