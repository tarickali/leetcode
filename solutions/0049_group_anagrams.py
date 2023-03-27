"""
title : 0049_group_anagrams.py
create : @tarickali 23/03/27
update : @tarickali 23/03/27
"""

from collections import defaultdict
from functools import reduce


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = reduce(lambda x, y: x + y, sorted(s), "")
            anagrams[key].append(s)
        return list(anagrams.values())
