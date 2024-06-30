"""
title : 0072_edit_distance.py
create : @tarickali 23/05/19
update : @tarickali 23/05/19
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def recurse(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            res = None
            if i == 0:
                res = j
            elif j == 0:
                res = i
            elif word1[i - 1] == word2[j - 1]:
                res = recurse(i - 1, j - 1)
            else:
                res = 1 + min(
                    recurse(i - 1, j),  # delete character from word1
                    recurse(i, j - 1),  # insert character to word1
                    recurse(i - 1, j - 1),  # replace character of word1
                )
            memo[(i, j)] = res
            return res

        return recurse(len(word1), len(word2))
