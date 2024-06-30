"""
title : 2849_determine_if_a_cell_is_reachable_at_a_given_time.py
create : @tarickali 23/11/07
update : @tarickali 23/11/07
"""


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        norm = max(abs(sx - fx), abs(sy - fy))
        return norm <= t if norm else t != 1
