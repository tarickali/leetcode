"""
title : 0278_first_bad_version.py
create : @tarickali 23/03/29
update : @tarickali 23/03/29
"""


def isBadVersion(version: int) -> bool:
    ...


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        bad = n
        while l <= r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                bad = m
                r = m - 1
            else:
                l = m + 1
        return bad
