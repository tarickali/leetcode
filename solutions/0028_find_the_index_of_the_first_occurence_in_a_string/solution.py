"""
title : 0028_find_the_index_of_the_first_occurence_in_a_string.py
create : @tarickali 23/06/13
update : @tarickali 23/06/13
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1
