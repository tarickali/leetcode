"""
title : 1503_last_moment_before_all_ants_fall_out_of_a_plank.py
create : @tarickali 23/11/04
update : @tarickali 23/11/04
"""


class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        t = 0
        while left and right:
            t += 1
            left = [pos - 1 for pos in left if pos > 0]
            right = [pos + 1 for pos in right if pos < n]

        if not left and not right:
            return t - 1
        elif not left:
            return t + n - min(right)
        elif not right:
            return t + max(left)
