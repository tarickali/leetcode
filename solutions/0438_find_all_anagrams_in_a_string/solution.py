"""
title : 0438_find_all_anagrams_in_a_string.py
create : @tarickali 23/04/04
update : @tarickali 23/04/04
"""

from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        indices = []
        target = Counter(p)
        counts = Counter(s[: len(p)])

        if counts == target:
            indices.append(0)

        for i in range(1, len(s) - len(p) + 1):
            counts.subtract({s[i - 1]: 1})
            counts.update({s[i + len(p) - 1]: 1})
            if counts == target:
                indices.append(i)

        return indices
