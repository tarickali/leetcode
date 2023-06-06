"""
title : 0994_rotting_oranges.py
create : @tarickali 23/06/05
update : @tarickali 23/06/05
"""

from queue import Queue


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        def search(i: int, j: int) -> None:
            frontier = Queue()
            seen = set()

            frontier.put((i, j))
            seen.add((i, j))
            times[(i, j)] = 0

            while not frontier.empty():
                x, y = frontier.get()
                explored.add((x, y))
                for p, q in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (
                        p < 0
                        or p >= len(grid)
                        or q < 0
                        or q >= len(grid[p])
                        or (p, q) in seen
                    ):
                        continue
                    if grid[p][q] != 0:
                        frontier.put((p, q))
                    seen.add((p, q))
                    if grid[p][q] == 0:
                        continue
                    elif grid[p][q] == 1:
                        times[(p, q)] = min(
                            times.get((p, q), float("inf")), times[(x, y)] + 1
                        )
                    else:  # grid[p][q] == 2
                        times[(p, q)] = 0

        explored = set()
        times = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    continue
                elif grid[i][j] == 0:
                    explored.add((i, j))
                else:  # grid[i][j] == 2
                    search(i, j)

        if len(explored) != len(grid) * len(grid[0]):
            return -1
        return max(times.values(), default=0)
