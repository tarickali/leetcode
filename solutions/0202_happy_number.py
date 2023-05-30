"""
title : 0202_happy_number.py
create : @tarickali 23/05/30
update : @tarickali 23/05/30
"""

from functools import reduce


class Solution:
    def isHappy(self, n: int) -> bool:
        vals = set()
        x = n
        for _ in range(n):
            x = reduce(lambda a, b: a + int(b) ** 2, str(x), 0)
            if x == 1:
                return True
            if x in vals:
                return False
            vals.add(x)
