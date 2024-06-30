"""
title : 0079_word_search.py
create : @tarickali 23/05/21
update : @tarickali 23/05/21
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def neighbors(i: int, j: int) -> list[tuple[int, int]]:
            N = []
            if i > 0:
                N.append((i - 1, j))
            if j > 0:
                N.append((i, j - 1))
            if i < len(board) - 1:
                N.append((i + 1, j))
            if j < len(board[i]) - 1:
                N.append((i, j + 1))
            return N

        def backtrack(i: int, j: int) -> bool:
            explored = set()

            def recurse(i: int, j: int, k: int) -> bool:
                nonlocal explored
                if (i, j) in explored:
                    return False
                if board[i][j] != word[k]:
                    return False
                if board[i][j] == word[k] and k == len(word) - 1:
                    return True

                explored.add((i, j))
                for p, q in neighbors(i, j):
                    if recurse(p, q, k + 1):
                        return True
                explored.remove((i, j))
                return False

            return recurse(i, j, 0)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i, j):
                    return True
        return False
