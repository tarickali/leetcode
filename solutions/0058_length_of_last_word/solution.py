"""
title : 0058_length_of_last_word.py
create : @tarickali 23/05/18
update : @tarickali 23/05/18
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
