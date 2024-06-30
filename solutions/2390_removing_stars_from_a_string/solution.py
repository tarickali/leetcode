"""
title : 2390_removing_stars_from_a_string.py
create : @tarickali 23/05/14
update : @tarickali 23/05/14
"""


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
