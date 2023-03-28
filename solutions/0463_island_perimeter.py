"""
title : 0463_island_perimeter.py
create : @tarickali 23/03/28
update : @tarickali 23/03/28
"""


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
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

        def find_island(grid) -> tuple[int, int]:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        return i, j
            return -1, -1

        perimeter = 0

        i, j = find_island(grid)
        stack = [(i, j)]
        visited = {(i, j)}

        while len(stack) != 0:
            ur, uc = stack.pop()
            land_around = 0
            for vr, vc in neighbors(grid, ur, uc):
                if grid[vr][vc] == 0:
                    continue
                land_around += 1
                if (vr, vc) not in visited:
                    stack.append((vr, vc))
                    visited.add((vr, vc))
            perimeter += 4 - land_around
        return perimeter
