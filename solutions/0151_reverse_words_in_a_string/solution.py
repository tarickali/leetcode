"""
title : 0151_reverse_words_in_a_string.py
create : @tarickali 23/05/18
update : @tarickali 23/05/18
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
