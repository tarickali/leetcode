"""
title : 1657_determine_if_two_strings_are_close.py
create : @tarickali 23/06/01
update : @tarickali 23/06/01
"""

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter_1 = Counter(word1)
        counter_2 = Counter(word2)

        return counter_1.keys() == counter_2.keys() and sorted(
            counter_1.values()
        ) == sorted(counter_2.values())
