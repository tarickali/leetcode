"""
title : 1071_greatest_common_divisor_of_strings.py
create : @tarickali 23/05/27
update : @tarickali 23/05/27
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        y = str1 if len(str1) < len(str2) else str2
        x = ""
        for i in reversed(range(len(y))):
            c = y[: i + 1]
            if set(str1.split(c)) == set(str2.split(c)) == {""}:
                x = c
                break
        return x
