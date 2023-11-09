"""
title : 0130_surrounded_regions.py
create : @tarickali 23/11/08
update : @tarickali 23/11/08
"""

from queue import Queue


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def bfs(s: tuple[int, int]) -> list[tuple[int, int]]:
            queue = Queue()
            seen = set()

            queue.put(s)
            seen.add(s)

            captured = True
            while not queue.empty():
                x = queue.get()
                xi, xj = x
                for y in [(xi + 1, xj), (xi - 1, xj), (xi, xj + 1), (xi, xj - 1)]:
                    yi, yj = y
                    if yi >= len(board) or yi < 0 or yj >= len(board[yi]) or yj < 0:
                        captured = False
                        continue
                    if board[yi][yj] == "X" or y in explored or y in seen:
                        continue
                    queue.put(y)
                    seen.add(y)
                explored.add(x)
            return seen, captured

        explored = set()
        convert = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X" or (i, j) in explored:
                    continue
                seen, captured = bfs((i, j))
                if captured:
                    convert |= seen

        for i, j in convert:
            board[i][j] = "X"
