"""
title : 0455_assign_cookies.py
create : @tarickali 23/12/31
update : @tarickali 23/12/31
"""


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)

        cnt = 0
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                cnt += 1
                i += 1
                j += 1
            else:
                i += 1
        return cnt
