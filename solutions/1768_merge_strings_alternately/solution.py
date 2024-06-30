"""
title : 1768_merge_strings_alternately.py
create : @tarickali 23/05/16
update : @tarickali 23/05/16
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        n = len(word1)
        m = len(word2)
        k = min(n, m)

        for i in range(k):
            merged += word1[i] + word2[i]
        for i in range(k, n):
            merged += word1[i]
        for i in range(k, m):
            merged += word2[i]
        return merged

    def mergeAlternately(self, word1: str, word2: str) -> str:
        k = min(len(word1), len(word2))
        merged = "".join([a + b for a, b in list(zip(word1, word2))])
        merged += word1[k:]
        merged += word2[k:]
        return merged

    def mergeAlternately(self, word1: str, word2: str) -> str:
        k = min(len(word1), len(word2))
        return (
            "".join([a + b for a, b in list(zip(word1, word2))]) + word1[k:] + word2[k:]
        )
