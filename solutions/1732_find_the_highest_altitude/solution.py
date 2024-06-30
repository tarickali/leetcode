"""
title : 1732_find_the_highest_altitude.py
create : @tarickali 23/05/14
update : @tarickali 23/05/14
"""


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        best = 0
        curr = 0
        for diff in gain:
            curr += diff
            best = max(best, curr)
        return best
