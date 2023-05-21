"""
title : 0139_word_break.py
create : @tarickali 23/05/20
update : @tarickali 23/05/20
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        wordset = set(wordDict)

        for i in range(n):
            sub = ""
            for j in range(i, n):
                sub += s[j]
                if sub in wordset and (i == 0 or memo[0][i - 1]):
                    memo[i][j] = True
                    memo[0][j] = True

        return memo[0][n - 1]
