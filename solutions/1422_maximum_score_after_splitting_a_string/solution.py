"""
title : 1422_maximum_score_after_splitting_a_string.py
create : @tarickali 23/12/22
update : @tarickali 23/12/22
"""

from collections import Counter


class Solution:
    def maxScore(self, s: str) -> int:
        best = 0
        for i in range(1, len(s)):
            best = max(best, Counter(s[:i]).get("0", 0) + Counter(s[i:]).get("1", 0))
        return best
