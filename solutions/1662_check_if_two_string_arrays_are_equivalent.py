"""
title : 1662_check_if_two_string_arrays_are_equivalent.py
create : @tarickali 23/12/02
update : @tarickali 23/12/02
"""


class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)
