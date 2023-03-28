"""
title : 0049_group_anagrams.py
create : @tarickali 23/03/27
update : @tarickali 23/03/27
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
        return list(anagrams.values())
