"""
title : 1926_nearest_exit_from_entrance_in_maze.py
create : @tarickali 23/05/29
update : @tarickali 23/05/29
"""

from queue import Queue


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        s = tuple(entrance)

        q = Queue()
        seen = set()
        dist = {}

        q.put(s)
        seen.add(s)
        dist[s] = 0
        while not q.empty():
            i, j = q.get()

            for r, c in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (
                    (r, c) in seen
                    or r < 0
                    or r >= len(maze)
                    or c < 0
                    or c >= len(maze[r])
                    or maze[r][c] == "+"
                ):
                    continue
                q.put((r, c))
                seen.add((r, c))
                dist[(r, c)] = dist[(i, j)] + 1
                if r == 0 or c == 0 or r == len(maze) - 1 or c == len(maze[i]) - 1:
                    return dist[(r, c)]

        return -1
