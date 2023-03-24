"""
title : 0205_isomorphic_strings.py
create : @tarickali 23/03/24
update : @tarickali 23/03/24
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)

        forward_mapping = {}
        reverse_mapping = {}
        for i in range(n):
            forward_mapping[s[i]] = t[i]
            reverse_mapping[t[i]] = s[i]

        x = ""
        y = ""
        for i in range(n):
            x += forward_mapping[s[i]]
            y += reverse_mapping[t[i]]

        return x == t and y == s
