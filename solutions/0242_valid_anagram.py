"""
title : 0242_valid_anagram.py
create : @tarickali 23/05/17
update : @tarickali 23/05/17
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
